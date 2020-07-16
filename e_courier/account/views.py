from django.db.models import Q
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse, get_object_or_404
from django.conf import settings
import stripe
import json
from django.views import View
from django.views.generic import ListView
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from django.urls import reverse_lazy
from sympy.physics.units import cd

from delivery_service.forms import DelevaryInfoForm
from industry.models import PriceSet, Industry
from .models import Profile, contact
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,TemplateView,DetailView
# Create your views here.
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ContactForm
from delivery_service.models import DeliveryProduct, DelevaryInfo
from django.urls import reverse
from django.contrib.auth import authenticate
from django.db.models import Sum,Count


stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def all_delivery_for_show_user(request):
    orders = DelevaryInfo.objects.filter().order_by('-id')
    # orders = delivery_product.objects.filter().order_by('-Date')
    return render(request, 'accounts/delivery_details_show_for_user.html', {'orders': orders})
def login(request):
    if request.method =="POST":
        # username = request.POST.get('username')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not create")
        else:
            print("Someone tried to login and falied!")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})

def SignUp(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        print(request.user)
        profile_, _ = Profile.objects.get_or_create(user=request.user)
        print(profile_)
        p_form = ProfileUpdateForm(instance=profile_)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/profile.html', context)

class help(TemplateView):
    template_name = 'accounts/help.html'


class customer_service(View):
    def get(self, request):
        return render(request,'accounts/customer_service.html')
    def post(self, request):
        print(request.POST)
        factoryname = request.POST.get('factoryname')
        email = request.POST.get('email')
        Message = request.POST.get('Message')
        book_details = contact(factoryname=factoryname, email=email, Message=Message)
        book_details.save()
        return redirect('/home')


def client_see_driver_details(request):
    order = DelevaryInfo.objects.filter().order_by('-id')
    key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request, 'accounts/client_see_driver_details.html', {'order': order, 'key': key})



@login_required
def rating_enter(request, order_id):
    order = DelevaryInfo.objects.get(id=order_id)
    if request.POST:
        form = DelevaryInfoForm(request.POST, instance=order)
        if form.is_valid():
            if form.save():
                return redirect(reverse('accounts:client_see_driver_details'), messages.success(request, 'Successfully rating create', 'alert-success'))
            else:
                return redirect(reverse('accounts:client_see_driver_details'), messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect(reverse('accounts:client_see_driver_details'), messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = DelevaryInfoForm(instance=order)
        return render(request, 'accounts/driver_rating_create.html', {'form': form})

def charge(request, delivery_id):
    order = DelevaryInfo.objects.get(id=delivery_id)
    price = PriceSet.objects.get(id=order.industry_id)
    if request.method == 'POST':
        print(price.price)
        charge =stripe.Charge.create(
            amount=str(price.price),
            currency='usd',
            description='Courier Payment',
            source=request.POST['stripeToken'],
        )
    return render(request,'accounts/charge.html', {'order': order})

def totalBill(request):
    total = DelevaryInfo.objects.all()
    order = []
    for delivery_info in total:
        print(delivery_info.client.user)
        if delivery_info.client.user == request.user:
            if delivery_info.order.order_status == '0':
                print(delivery_info.client)
                order += [delivery_info.industry.price]
    print(order)
    sum = 0
    for i in range(len(order)):
        sum+=order[i]
    print(sum)
    result = DelevaryInfo.objects.values('client').order_by('client').annotate(count=Count('client')).annotate(total_price=Sum('industry'))
    return render(request,'accounts/totalBill.html', {'result': result, 'total': total,'sum': sum})

@login_required
def SearchResultsView(request):
    queryset_list = PriceSet.objects.all()
    # import pdb;
    # pdb.set_trace()
    query = request.GET.get("q")

    if query:
        queryset_list=queryset_list.filter(
            Q(location1__icontains=query) |
            Q(location2__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 4)  # Show 25 contacts per page
    page_request_var = "pageList"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context={
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var
    }
    return render(request, "accounts/priceSet.html", context)




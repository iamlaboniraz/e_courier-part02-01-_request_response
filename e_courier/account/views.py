from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy
from .models import Profile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,TemplateView
# Create your views here.
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from delivery_service.models import delivery_product, DelevaryInfo
from django.urls import reverse
from django.contrib.auth import authenticate
@login_required
def all_delivery_for_show_user(request):
    orders = delivery_product.objects.all().order_by('-Date')
    return render(request, 'accounts/delivery_details_show_for_user.html', {'orders': orders})
def login(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
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
        return render(request,'login.html',{})

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

class customer_service(TemplateView):
    template_name = 'accounts/customer_service.html'

# def client_see_driver_details(request):
#     order = DelevaryInfo.objects.get()
#     print(order)
#     context = {
#         'order': order,
#     }
#     return render(request,'accounts/client_see_driver_details.html',context)
def client_see_driver_details(request):
    order = DelevaryInfo.objects.filter()
    return render(request, 'accounts/client_see_driver_details.html', {'order': order})


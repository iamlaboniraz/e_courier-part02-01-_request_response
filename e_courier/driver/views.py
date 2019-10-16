from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from .models import driver_profile
from django.contrib.auth.decorators import login_required
from .forms import DriverRegisterForm, DriverUpdateForm, DriverProfileUpdateForm,deliverForm
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView
from delivery_service.models import delivery_product
from django.views import View

# Create your views here.

#### registration part####### 
def driver_login(request):
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Account not create")
        else:
            print("Someone tried to login and falied!")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request,'account/driver_login.html',{})

def DriverSignUp(request):
    if request.method == 'POST':
        form = DriverRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account has been created! You are now able to log in')

            return redirect(reverse('driver:driver_login'))
    else:
        form = DriverRegisterForm()
    return render(request, 'account/driver_signup.html', {'form': form})

@login_required
def driver_profile_page(request):
    if request.method == 'POST':
        u_form = DriverUpdateForm(request.POST, instance=request.user)
        p_form = DriverProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.driver_profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            # return redirect(reverse('driver:driver_profile_page'))
            return redirect(reverse('driver:driver_profile_page'), messages.success(request, 'Order was successfully update.', 'alert-success'))

    else:
        u_form = DriverUpdateForm(instance=request.user)
        print(request.user)
        profile_page_, _ = driver_profile.objects.get_or_create(user=request.user)
        print(profile_page_)
        p_form = DriverProfileUpdateForm(instance=profile_page_)
        print(p_form)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'driver': request.user.driver_profile
    }

    return render(request, 'account/driver_profile.html', context)


################################
def driver_form(request):
    if request.method == 'POST':
        form_data=deliverForm(request.POST,request.FILES)
        if form_data.is_valid():
            form_data.save()
            new_form=deliverForm()
        else:
            note="failed.Try again!!"
        return render(request,'driver_form.html',{'form':new_form})
    else:
        form_data = deliverForm()
        return render(request,'driver_form.html',{'form':form_data})

def Active_driver(request):
    driver_list = driver_profile.objects.all().filter(status='Active')
    context = {
        'driver_list':driver_list
    }
    return render(request,'driver_list.html',context)

def driver(request):
    driver_list = driver_profile.objects.all()
    context = {
        'driver_list':driver_list
    }
    return render(request,'driver_list.html',context)

def edit(request,id):
	driver_list=driver_profile.objects.get(pk=id)
	print(driver_list)
	return render(request,'edit.html',{'driver_list':driver_list})

def update(request, id):
    driver_list = driver_profile.objects.get(pk=id)
    driver_list.status = request.GET['status']
    driver_list.name = request.GET['name']
    driver_list.car_details = request.GET['car_details']
    driver_list.phone = request.GET['phone']
    driver_list.save()
    return redirect("/")


class driver_see_the_request(TemplateView):
    template_name = 'tasks.html'

# class DeliveryUpdate(View):
#     def post(self, request, id):
#         driver = driver_profile.objects.get(user__id = int(request.POST["user"]))
#         dp = delivery_product.objects.get(id=int(request.POST["object"]))
#         driver.task = dp
#         driver.status = "Onrequest"
#         driver.save()
#         print(s)
#         print(driver)
#         print(dp)
#         context = {
#         'driver':driver,
#         'dp':dp}
#         return render(request,'tasks.html',context)




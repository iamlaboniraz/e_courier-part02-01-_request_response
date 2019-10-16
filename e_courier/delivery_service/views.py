from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

from account.models import Profile
from delivery_service.models import DelevaryInfo
from .forms import deliverForm
from driver.models import driver_profile
from .models import delivery_product,types_of_product
from django.http import  JsonResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.views.generic import DetailView
from django.db.models import ProtectedError
from django.views.generic import ListView, TemplateView
from driver.models import driver_profile
# Create your views here.
@login_required
def all_delivery(request):
    orders = delivery_product.objects.all().order_by('-Date').filter(order_status='1')
    return render(request, 'index_delivery_details.html', {'orders': orders})

@login_required
def all_latest_delivery_order(request):
    orders = delivery_product.objects.all().order_by('-Date').filter(order_status='0')
    return render(request, 'all_latest_delivery_order.html', {'orders': orders})


@login_required
def show(request, order_id):
    order = delivery_product.objects.filter(id=order_id)
    return render(request, 'show_delivery.html', {'order': order})

def delivery_request(request):
    if request.method == 'POST':
        form_delivery=deliverForm(request.POST,request.FILES)
        if form_delivery.is_valid():
            delivery_product_info = form_delivery.save()
            client = Profile.objects.get(user=request.user)
            DelevaryInfo(client=client, order=delivery_product_info).save()
            note = "Thanks for your request!! Wait a few minutes!! Car is on the way!!"
            new_form_delivery=deliverForm()
        else:
            note="failed.Try again!!"
        return render(request,'delivery_form.html',{'deliveryform':new_form_delivery,'note':note})
    else:
        form_delivery = deliverForm()
        return render(request,'delivery_form.html',{'deliveryform':form_delivery})


@login_required
def edit_delivery(request, order_id):
    order = delivery_product.objects.get(id=order_id)
    if request.POST:
        form = deliverForm(request.POST, instance=order)
        if form.is_valid():
            if form.save():
                return redirect(reverse('delivery_service:edit_delivery', args=(order.id,)), messages.success(request, 'Order was successfully updated.', 'alert-success'))
            else:
                return redirect(reverse('delivery_service:edit_delivery', args=(order.id,)), messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            print(form.errors)
            return redirect(reverse('delivery_service:edit_delivery', args=(order.id,)), messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = deliverForm(instance=order)
        return render(request, 'edit_delivery.html', {'form': form})

@login_required
def delivery_destroy(request, order_id):
    order = delivery_product.objects.get(id=order_id)
    try:
        order.delete()
    except ProtectedError:
        error_message = "This object can't be deleted!!"
        return JsonResponse(error_message)
    # order.delete()
    return redirect(reverse('delivery_service:all_delivery'), messages.success(request, 'Order was successfully deleted.', 'alert-success'))





# class DeliveryDetail(DetailView):
#     template_name='delivery_detail_view.html'
#     def get_object(self):
#         id_=self.kwargs.get("id")
#         return get_object_or_404(delivery_product,id=id_)




def DeliveryDetail(request, id=None):

    obj= get_object_or_404(delivery_product, id=id)
    
    context= {'obj': obj,
              }
    
    return render(request, 'delivery_detail_view.html', context)
# def edit_delivery(request,order_id):   
#     order=delivery_product.objects.get(pk=order_id)
#     context={
#     'order': order,
#     }
#     return render(request,'edit_delivery.html',context)

# def update_delivery(request, order_id):
#     order=delivery_product.objects.get(pk=order_id)
#     order.from_location = request.GET['from_location']
#     order.to_location = request.GET['to_location']
#     order.product_type = request.GET['product_type']
#     order.Date = request.GET['Date']
#     order.phone = request.GET['phone']
#     order.payment_option = request.GET['payment_option']
#     order.order_status = request.GET['order_status']
#     order.save()
#     return redirect(reverse('delivery_service:edit_delivery', args=(order.order_id,)))

def wait_sms(request):
    return render(request,'wait.html')

def see(request,my_id):
    obj = get_object_or_404(delivery_product,id=my_id)
    context={
        'object':obj
    }
    return render(request,"delivery_view_for_driver_send.html", context)


@login_required
def send(request):
    delivery_info_list = DelevaryInfo.objects.filter(driver=None)
    order = []
    for delivery_info in delivery_info_list:
        order += [delivery_info.order]

    return render(request, 'driver_see.html', {'order': order})


# @login_required
# def click_for_send_driver_details(request,my_id):
#     object = driver_profile.objects.filter(user=request.user)
#     # object = driver_profile.objects.filter(id=my_id)
#     # print(object)
#     # driver = get_object_or_404(driver_profile, pk=obj.pk)
#     obj = driver_profile.objects.get(user__username=request.user.username)
#     # print(obj)
#     context={
#         'object': object,
#         'obj': obj
#         # 'driver':driver
#     }
#     return render(request,'click_for_send_driver_details.html', context)


@login_required
def click_for_send_driver_details(request,my_id):
    model = get_object_or_404(delivery_product,id=my_id)

    object = driver_profile.objects.get(user=request.user)

    delivery_details = DelevaryInfo.objects.get(order=model)
    delivery_details.driver = object
    delivery_details.save()
    obj = driver_profile.objects.get(user__username=request.user.username)
    context = {
        'obj': obj,
        'model':model
    }
    # print(driver)
    return render(request, 'click_for_send_driver_details.html', context)

def client_see_driver_details(request, request_id,**kwargs):
    model = get_object_or_404(driver_profile, id=request_id)
    if model.id:
        driver = driver_profile.objects.filter(user=request.user)

    else:
        driver = None

    context = {
        'request': model,
        'driver': driver
    }
    return render(request, 'accounts/client_see_driver_details.html', context)



# def edit_delivery(request,order_id):
#     order=delivery_product.objects.get(pk=order_id)
#     context={
#     'order': order,
#     }
#     return render(request,'now_ready_for_send_it_client.html',context)

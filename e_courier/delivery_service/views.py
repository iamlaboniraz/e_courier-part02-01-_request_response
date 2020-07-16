from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
import json
from account.models import Profile
from delivery_service.models import DelevaryInfo, OrderUpdate
from industry.models import Location
from .forms import deliverForm, deliverFormEdit, OrderUpdateForm
from driver.models import DriverProfile
from .models import DeliveryProduct,TypesOfProduct
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.views.generic import DetailView
from django.db.models import ProtectedError
from django.views.generic import ListView, TemplateView

# Create your views here.
@login_required
def all_delivery(request):
    orders = DeliveryProduct.objects.all().order_by('-Date').filter(order_status='1')
    return render(request, 'index_delivery_details.html', {'orders': orders})

@login_required
def all_latest_delivery_order(request):
    orders = DelevaryInfo.objects.all()
    return render(request, 'all_latest_delivery_order.html', {'orders': orders})

@login_required
def delivery_track_update(request):
    track = OrderUpdate.objects.all().order_by('-order_id')
    return render(request,'system_admin_track_update.html',{'track':track})

@login_required
def delivery_track_add(request):
    if request.method == 'POST':
        add = OrderUpdateForm(request.POST, request.FILES)
        if add.is_valid():
            add_info = add.save()
            new_add_info = OrderUpdateForm()
        else:
            note = "failed.Try again!!"
        return render(request, 'add_track_update.html', {'new_add_info': new_add_info})
    else:
        add = OrderUpdateForm()
        return render(request, 'add_track_update.html', {'new_add_info': add})

# def track_id_separate(request,order_id):
#     track_id = OrderUpdate.objects.filter(id=order_id)
#     return render(request,)

@login_required
def show(request, order_id):
    order = DelevaryInfo.objects.filter(id=order_id)
    return render(request, 'show_delivery.html', {'order': order})


def delivery_request(request):
    if request.method == 'POST':
        form_delivery=deliverForm(request.POST,request.FILES)
        if form_delivery.is_valid():
            delivery_product_info = form_delivery.save()
            update = OrderUpdate(order_id=delivery_product_info.id, update_desc="The order has been placed")
            update.save()
            id = delivery_product_info.id
            client = Profile.objects.get(user=request.user)
            DelevaryInfo(client=client, order=delivery_product_info).save()
            note = "Thanks for your request!! Wait a few minutes!! Car is on the way!!"
            new_form_delivery=deliverForm()
        else:
            note="failed.Try again!!"
        return render(request,'delivery_form.html',{'deliveryform': new_form_delivery,'note': note,'id': id})
    else:
        form_delivery = deliverForm()
        return render(request,'delivery_form.html', {'deliveryform':form_delivery})


@login_required
def edit_delivery(request, order_id):
    order = DeliveryProduct.objects.get(id=order_id)
    if request.POST:
        form = deliverFormEdit(request.POST, instance=order)
        if form.is_valid():
            if form.save():
                return redirect(reverse('delivery_service:edit_delivery', args=(order.id,)), messages.success(request, 'Order was successfully updated.', 'alert-success'))
            else:
                return redirect(reverse('delivery_service:edit_delivery', args=(order.id,)), messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            print(form.errors)
            return redirect(reverse('delivery_service:edit_delivery', args=(order.id,)), messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = deliverFormEdit(instance=order)
        return render(request, 'edit_delivery.html', {'form': form})

@login_required
def delivery_destroy(request, order_id):
    order = DeliveryProduct.objects.get(id=order_id)
    try:
        order.delete()
    except ProtectedError:
        error_message = "This object can't be deleted!!"
        return JsonResponse(error_message)
    # order.delete()
    return redirect(reverse('delivery_service:all_delivery'), messages.success(request, 'Order was successfully deleted.', 'alert-success'))




def DeliveryDetail(request, id=None):
    obj = get_object_or_404(DeliveryProduct, id=id)
    
    context= {'obj': obj,
              }
    
    return render(request, 'delivery_detail_view.html', context)

def wait_sms(request):

    return render(request,'wait.html')

@login_required
def driver_choose_present_location(request):
    return render(request,'driver_choose_present_location.html')
def see(request,my_id):
    obj = get_object_or_404(DeliveryProduct, id=my_id)
    context = {
        'object': obj
    }
    return render(request, "delivery_view_for_driver_send.html", context)


@login_required
def send(request):
    delivery_info_list = DelevaryInfo.objects.filter(driver=None)
    order = []
    for delivery_info in delivery_info_list:
        order += [delivery_info.order]

    return render(request, 'driver_see.html', {'order': order})


@login_required
def GazipurZone(request):
    delivery_info_list = DelevaryInfo.objects.filter(driver=None)
    order = []
    for delivery_info in delivery_info_list:
        order += [delivery_info.order]

    return render(request, 'for_gajipur_zone.html', {'order': order})

@login_required
def BonaniZone(request):
    delivery_info_list = DelevaryInfo.objects.filter(driver=None)
    order = []
    for delivery_info in delivery_info_list:
        order += [delivery_info.order]

    return render(request, 'for_Bonani_zone.html', {'order': order})


@login_required
def click_for_send_driver_details(request,my_id):
    x= get_object_or_404(DelevaryInfo,id=my_id)
    model = get_object_or_404(DeliveryProduct,id=my_id)

    object = DriverProfile.objects.get(user=request.user)

    delivery_details = DelevaryInfo.objects.get(order=model)
    delivery_details.driver = object
    delivery_details.save()
    obj = DriverProfile.objects.get(user__username=request.user.username)
    context = {
        'obj': obj,
        'model': model,
        'x':x
    }
    # print(driver)
    return render(request, 'click_for_send_driver_details.html', context)



def cancel_ride(request):
    order = DelevaryInfo.objects.all()
    for delivery_info in order:
        print(delivery_info.driver)

    # try:
    #     order.delete()
    # except ProtectedError:
    #     error_message = "This object can't be deleted!!"
    #     return JsonResponse(error_message)
    # # order.delete()
    return render(request,'click_for_send_driver_details.html')

def client_see_driver_details(request, request_id,**kwargs):
    model = get_object_or_404(DriverProfile, id=request_id)
    if model.id:
        driver = DriverProfile.objects.filter(user=request.user)

    else:
        driver = None
    context = {
        'request': model,
        'driver': driver,
    }
    return render(request, 'accounts/client_see_driver_details.html', context)

# def tracker(request):
#     if request.method=="POST":
#         orderId = request.POST.get('orderId', '')
#         phone = request.POST.get('phone', '')
#         try:
#             order = DeliveryProduct.objects.filter(id=orderId, phone=phone)
#             if len(order)>0:
#                 update = OrderUpdate.objects.filter(order_id=orderId)
#                 updates = []
#                 for item in update:
#                     updates.append({'text': item.update_desc, 'time': item.timestamp})
#                     response = json.dumps(updates, default=str)
#                 return HttpResponse(response)
#             else:
#                 return HttpResponse('{}')
#         except Exception as e:
#             return HttpResponse('{}')
#
#     return render(request, 'tracker.html')



def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        # phone = request.POST.get('phone', '')
        try:
            # order = DeliveryProduct.objects.filter(id=orderId, phone=phone)
            order = DeliveryProduct.objects.filter(id=orderId)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                # value1=[]
                # value2=[]
                for item in update:
                    updates.append({'text': item.longitude,'number': item.latitude,'time': item.timestamp})
                    response = json.dumps(updates, default=str)
                    # x = item.longitude
                    # y=item.latitude
                    # # print(" x = ",x,"y = ",y)
                    # value1.append(x)
                    # value2.append(y)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'tracker.html')

class ClientChart(TemplateView):
    template_name = 'ClientChart.html'


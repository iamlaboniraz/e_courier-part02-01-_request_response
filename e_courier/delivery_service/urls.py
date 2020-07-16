from django.urls import path
from .import views
from .views import(
   delivery_request,
   wait_sms
)
app_name='delivery_service'
urlpatterns = [
      path('', views.delivery_request, name='delivery_request'),
      # path('sms_send/', views.sms_send, name='sms_send'),
      path('wait_sms/',views.wait_sms,name='wait_sms'),
      path('all_delivery/',views.all_delivery,name='all_delivery'),
      path('tracker/',views.tracker,name='tracker'),
      path('all_latest_delivery_order/',views.all_latest_delivery_order,name='all_latest_delivery_order'),
      path('show/<order_id>/',views.show,name='show'),
      # path('edit_delivery/<int:order_id>/',views.edit_delivery,name="edit_delivery" ),
      path('edit_delivery/<order_id>/', views.edit_delivery,name='edit_delivery'),
      # path('update_delivery/<order_id>/', views.update_delivery,name='update_delivery'),
      path('DeliveryDetail/<int:id>/',views.DeliveryDetail,name="DeliveryDetail" ),
      path('delivery_destroy/<order_id>/',views.delivery_destroy,name="delivery_destroy" ),
      path('cancel_ride/',views.cancel_ride,name="cancel_ride" ),

      path('see/<int:my_id>/', views.see, name='see'),
      path('send/', views.send, name='send'),

      path('delivery_track_update/', views.delivery_track_update, name='delivery_track_update'),
      path('delivery_track_add/', views.delivery_track_add, name='delivery_track_add'),
      path('ClientChart/', views.ClientChart.as_view(), name='ClientChart'),
      path('GazipurZone/', views.GazipurZone, name='GazipurZone'),
      path('BonaniZone/', views.BonaniZone, name='BonaniZone'),
      path('click_for_send_driver_details/<int:my_id>/', views.click_for_send_driver_details, name='click_for_send_driver_details'),
      path('client_see_driver_details/<int:request_id>/', views.client_see_driver_details, name='client_see_driver_details'),
      path('driver_choose_present_location/',views.driver_choose_present_location,name="driver_choose_present_location"),
   ]
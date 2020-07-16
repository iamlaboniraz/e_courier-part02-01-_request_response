from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
app_name="driver"
urlpatterns = [
      path('', views.Active_driver, name='Active_driver'),
      path('driver/', views.driver, name='driver'),
      path('driver_form/', views.driver_form,name='driver_form'),
      path('edit/<id>/', views.edit,name='edit'),
      path('update/<id>/', views.update,name='update'),

      path('driver_login/', auth_views.LoginView.as_view(template_name='account/driver_login.html'), name='driver_login'),#driver
      path('logout/', auth_views.LogoutView.as_view(), name='logout'),
      
      path('DriverSignUp/', views.DriverSignUp, name='DriverSignUp'),#driver
      
      path('driver_profile_page/', views.driver_profile_page, name='driver_profile_page'),#driver
      path('driver_see_the_request/', views.driver_see_the_request.as_view(template_name='tasks.html'), name='driver_see_the_request'),

      # path('DeliveryUpdate/<int:id>/',views.DeliveryUpdate.as_view(),name="DeliveryUpdate" ),
      path('driver_see_delivery_details/',views.driver_see_delivery_details,name="driver_see_delivery_details" ),
      # path('ForShareLocation/',views.ForShareLocation,name="ForShareLocation"),
      path('livelocationshare/<int:id>/',views.livelocationshare,name="livelocationshare"),
      path('locationUpdate/<int:order_id>/',views.locationUpdate,name="locationUpdate"),
      path('ViewMapLocation/<int:id>/',views.ViewMapLocation,name="ViewMapLocation"),
]

from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
app_name='FactoryHead'
urlpatterns = [
    path('FactoryList/',views.FactoryList.as_view(),name='FactoryList'),
    path('FactoryEmployeeList/<int:pk>/',views.FactoryEmployeeList.as_view(), name='FactoryEmployeeList'),
    path('FactoryDetails/<int:pk>/',views.FactoryDetails.as_view(), name='FactoryDetails'),
    path('totalpayment/', views.totalpayment, name='totalpayment'),
    path('FactoryInvoicePrint/<int:pk>/', views.FactoryInvoicePrint.as_view(), name='FactoryInvoicePrint'),
    ]
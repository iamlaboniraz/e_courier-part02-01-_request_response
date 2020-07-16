from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
app_name='accounts'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp, name='signup'),

    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('help/', views.help.as_view(), name='help'),
    path('SearchResultsView/', views.SearchResultsView, name='SearchResultsView'),
    path('totalBill/', views.totalBill, name='totalBill'),
    path('customer_service/', views.customer_service.as_view(), name='customer_service'),
    path('all_delivery_for_show_user/', views.all_delivery_for_show_user, name='all_delivery_for_show_user'),
    path('client_see_driver_details/', views.client_see_driver_details, name="client_see_driver_details"),
    path('charge/<int:delivery_id>/', views.charge, name="charge"),
    path('rating_enter/<int:order_id>/', views.rating_enter, name="rating_enter"),
]
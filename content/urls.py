from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('customer/<str:pk>/', views.customer,name='customer'),
    path('product/', views.product),
    path('updateorder/<str:pk>/', views.CreateFrom,name='updateorder'),
    path('deleteorder/<str:pk>/', views.Deleteorder, name='deleteorder'),
    path('createorder/<str:pk>/', views.CreateOrder, name='createorder'),
    # path('createcustomer/', views.CreateCustomer, name='createcustomer'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.Loginpage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('user/', views.user, name='user'),
    path('setting/', views.profilesetting, name='setting'),
]

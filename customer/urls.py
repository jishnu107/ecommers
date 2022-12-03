from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('custlogin',views.custhome_page,name='custlogin'),
    path('custpass',views.custpass_page,name='custpass'),
    path('custcart',views.custcart_page,name='custcart'),
    path('custorder',views.custorder_page,name='custorder'),


]
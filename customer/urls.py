from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [
    path('custhome',views.custhome_page,name='custhome'),
    path('profile',views.profile_page,name='profile'),
    path('custpass',views.custpass_page,name='custpass'),
    path('custcart',views.custcart_page,name='custcart'),
    path('custorder',views.custorder_page,name='custorder'),
    path('viewproduct/<int:pid>',views.viewproduct_page,name='viewproduct'),
    path('remove_cart/<int:pid>',views.remove_item,name='remove_cart'),




]
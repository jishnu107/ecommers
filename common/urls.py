from django.urls import path
from . import views

app_name = 'common'
urlpatterns = [
    path('custreg',views.custreg_page,name='custreg'),
    path('sellreg',views.sellreg_page,name='sellreg'),
    path('selllogin',views.selllogin_page,name='selllogin'),
    path('custlogin',views.custlogin_page,name='custlogin'),
    path('email_exist',views.email_exist,name='email_exist'),








]
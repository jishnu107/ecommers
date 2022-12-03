from django.urls import path
from . import views

app_name = 'common'
urlpatterns = [
    path('homepage',views.home_page,name='homepage'),
    path('custreg',views.custreg_page,name='custreg'),
    path('sellreg',views.sellreg_page,name='sellreg'),
    path('selllogin',views.selllogin_page,name='selllogin'),
    path('addprod',views.addprod_page,name='addprod'),
    path('custlogin',views.custlogin_page,name='custlogin'),
    path('custlogin',views.custlogin_page,name='custlogin'),
    path('pass',views.pass_page,name='pass'),







]
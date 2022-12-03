from django.urls import path
from . import views

app_name = 'ecome_admin'
urlpatterns = [
    path('adminhome',views.adminhome_page,name='adminhome'),
    path('custview',views.custview_page,name='custview'),
    path('sellerview',views.sellview_page,name='sellerview'),
    path('sellapprove',views.sellapprove_page,name='sellapprove'),
    path('pass',views.pass_page,name='pass'),




]
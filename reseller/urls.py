from django.urls import path
from . import views

app_name = 'reseller'
urlpatterns = [
    path('sellerlogin',views.sellerhome_page,name='sellerlogin'),
    path('addroduct',views.addproduct_page,name='addproduct'),
    path('sellerpass',views.sellerpass_page,name='sellerpass'),
]
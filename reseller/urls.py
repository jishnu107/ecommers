from django.urls import path
from . import views

app_name = 'reseller'
urlpatterns = [
    path('sellerhome',views.sellerhome_page,name='sellerhome'),
    path('addroduct',views.addproduct_page,name='addproduct'),
    path('sellerpass',views.sellerpass_page,name='sellerpass'),
]
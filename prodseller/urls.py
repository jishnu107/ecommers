from django.urls import path
from . import views

app_name = 'prodseller'
urlpatterns = [
    path('sellerhome', views.sellerhome_page, name='sellerhome'),
    path('addproduct', views.addproduct_page, name='addproduct'),
    path('sellerpass', views.sellerpass_page, name='sellerpass'),
    path('catlog', views.catlog_page, name='catlog'),
    path('currentstock', views.currentstock_page, name='currentstock'),
    path('updatestock', views.updatestock_page, name='updatestock'),
]

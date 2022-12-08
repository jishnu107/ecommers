from django.shortcuts import render
from prodseller.models import Product


# Create your views here.

def custhome_page(request):
    all_products = Product.objects.all()
    return render(request,'customer/custhome.html',{'prods': all_products})
def custpass_page(request):
    return render(request,'customer/pass.html')
def custorder_page(request):
    return render(request,'customer/order.html')
def custcart_page(request):
    return render(request,'customer/cart.html')
def viewproduct_page(request):
    return render(request,'customer/viewproduct.html')
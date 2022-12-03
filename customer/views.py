from django.shortcuts import render

# Create your views here.

def custhome_page(request):
    return render(request,'customer/custlogin.html')
def custpass_page(request):
    return render(request,'customer/pass.html')
def custorder_page(request):
    return render(request,'customer/order.html')
def custcart_page(request):
    return render(request,'customer/cart.html')
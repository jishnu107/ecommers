from django.shortcuts import render
from common.models import Customer,Seller

# Create your views here.

def adminhome_page(request):
    return render(request,'ecomadmin/adminhome.html')
def custview_page(request):

    customers = Customer.objects.all()
    
    return render(request,'ecomadmin/custview.html',{'customer_list':customers})

def sellview_page(request):

    sellers = Seller.objects.all()

    return render(request,'ecomadmin/sellerview.html',{'seller_list':sellers})
def sellapprove_page(request):
    return render(request,'ecomadmin/sellapprove.html')
def pass_page(request):
    return render(request,'ecomadmin/pass.html')

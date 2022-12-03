from django.shortcuts import render
from common.models import Customer

# Create your views here.

def adminhome_page(request):
    return render(request,'ecomadmin/adminhome.html')
def custview_page(request):

    customers = Customer.objects.all()
    
    return render(request,'ecomadmin/custview.html',{'customer_list':customers})

def sellview_page(request):
    return render(request,'ecomadmin/sellerview.html')
def sellapprove_page(request):
    return render(request,'ecomadmin/sellapprove.html')
def pass_page(request):
    return render(request,'ecomadmin/pass.html')

from django.shortcuts import render

# Create your views here.

def sellerhome_page(request):
    return render(request,'reseller/selllogin.html')
def addproduct_page(request):
    return render(request,'reseller/addprod.html')
def sellerpass_page(request):
    return render(request,'reseller/pass.html')
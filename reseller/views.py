from django.shortcuts import render
from common.models import Seller
# Create your views here.

def sellerhome_page(request):
    seller_data = Seller.objects.get(id = request.session['seller'])
    return render(request,'reseller/sellhome.html',{'data':seller_data})
def addproduct_page(request):
    return render(request,'reseller/addprod.html')
def sellerpass_page(request):
    return render(request,'reseller/pass.html')
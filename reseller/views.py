from django.shortcuts import render
from common.models import Seller
from . models import Product


# Create your views here.


def sellerhome_page(request):
    seller_data = Seller.objects.get(id=request.session['seller'])
    return render(request, 'reseller/sellhome.html', {'data': seller_data})


def addproduct_page(request):
    if request.method == 'POST':
        product_name = request.POST['p_name']
        product_description = request.POST['p_description']
        product_number = request.POST['p_number']
        current_stock = request.POST['current_stock']
        product_image = request.FILES['p_image']
        price = request.POST['price']

        new_product = Product(product_name=product_name, product_description=product_description, product_number=product_number,
                              current_stock=current_stock, product_image=product_image, price=price)
        new_product.save()

    return render(request, 'reseller/addprod.html')


def sellerpass_page(request):
    return render(request, 'reseller/pass.html')


def catlog_page(request):
    return render(request, 'reseller/catlog.html')


def currentstock_page(request):
    return render(request, 'reseller/currentstock.html')


def updatestock_page(request):
    return render(request, 'reseller/updatestock.html')

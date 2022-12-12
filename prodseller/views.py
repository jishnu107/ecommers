from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from common.models import Seller
from . models import Product


# Create your views here.


def sellerhome_page(request):
    seller_data = Seller.objects.get(id=request.session['seller'])
    return render(request, 'prodseller/sellhome.html', {'data': seller_data})


def addproduct_page(request):
    msg = ''
    seller_data = Seller.objects.get(id=request.session['seller'])
    if request.method == 'POST':
        product_name = request.POST['p_name']
        product_description = request.POST['p_description']
        product_number = request.POST['p_number']
        current_stock = request.POST['current_stock']
        product_image = request.FILES['p_image']

        price = request.POST['price']

        new_product = Product(product_name=product_name, product_description=product_description, product_number=product_number,
                              current_stock=current_stock, product_image=product_image, price=price, seller_id=request.session['seller'])
        new_product.save()
        msg = "product added successfully"

    return render(request, 'prodseller/addprod.html',{'msg':msg,'data': seller_data})


def sellerpass_page(request):
    seller_data = Seller.objects.get(id=request.session['seller'])
    return render(request, 'prodseller/pass.html', {'data': seller_data})


def catlog_page(request):
    seller_products = Product.objects.filter(seller = request.session['seller'])
    seller_data = Seller.objects.get(id=request.session['seller'])

    return render(request, 'prodseller/catlog.html',{'products':seller_products,'data': seller_data})


def currentstock_page(request):
    seller_data = Seller.objects.get(id=request.session['seller'])


    return render(request, 'prodseller/currentstock.html', {'data': seller_data})


def updatestock_page(request):
    seller_data = Seller.objects.get(id=request.session['seller'])

    return render(request, 'prodseller/updatestock.html', {'data': seller_data})

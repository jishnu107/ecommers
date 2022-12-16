from django.shortcuts import render,redirect

# Create your views here.

from django.shortcuts import render
from common.models import Seller
from . models import Product
from django.http import JsonResponse


# Create your views here.


def sellerhome_page(request):
    seller_data = Seller.objects.get(id=request.session['seller'])
    return render(request, 'prodseller/sellhome.html', {'data': seller_data})


def addproduct_page(request):
    msg = ''
<<<<<<< HEAD
    
=======
    seller_data = Seller.objects.get(id=request.session['seller'])
>>>>>>> ceb488573cec40d75cee850743c070524a9d6001
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
    msg =''
    seller_data = Seller.objects.get(id=request.session['seller'])
    if request.method == 'POST':
        seller = Seller.objects.get(id = request.session['seller'])

        current_pass = request.POST['current_pass'] 
        new_pass = request.POST['new_pass'] 
        confirm_pass = request.POST['confirm_pass']

        if seller.seller_pass == current_pass:

            if new_pass == confirm_pass:
                 seller.seller_pass = new_pass
                 seller.save()
                 msg = 'Password changed succesfully'

            else:
                msg = 'Password does not match'

        else:
            msg = 'Incorrect Password'
    context =  {'msg':msg,
                'data': seller_data,
                }
    return render(request, 'prodseller/pass.html',context)


def catlog_page(request):
    seller_products = Product.objects.filter(seller = request.session['seller'])
    seller_data = Seller.objects.get(id=request.session['seller'])
    context ={'products':seller_products,
                'data': seller_data,
                }

    return render(request, 'prodseller/catlog.html',context)


def currentstock_page(request):
    seller_data = Seller.objects.get(id=request.session['seller'])

    context = {
        'data': seller_data,
    }
    return render(request, 'prodseller/currentstock.html',context)


def updatestock_page(request):
    seller_data = Seller.objects.get(id=request.session['seller'])
    product_data = Product.objects.filter(seller=request.session['seller'])

    if request.method == 'POST':
        new_stock = request.POST['new_stock']
        product_id = request.POST['productid']

        product = Product.objects.get(id=product_id)
        product.current_stock = product.current_stock + int(new_stock)

        product.save()
    context = {'prod_data': product_data,
                    'data': seller_data,
                    }


    return render(request, 'prodseller/updatestock.html',context)

def logout(request):
    del request.session['seller'] 
    request.session.flush()
    return redirect('common:selllogin')

def get_stock(request):
    id = request.POST['id']
    product =Product.objects.get(id=id)
    product_name = product.product_name
    current_stock = product.current_stock
    product_id = product.id
    return JsonResponse({'p_name':product_name,'stock':current_stock,'p_id':product_id})





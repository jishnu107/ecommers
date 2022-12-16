from django.shortcuts import render,redirect
from common.models import Customer,Seller
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def adminhome_page(request):
    return render(request,'ecomadmin/adminhome.html')
def custview_page(request):

    customers = Customer.objects.all()
    
    return render(request,'ecomadmin/custview.html',{'customer_list':customers})

def sellview_page(request):
    sellers = Seller.objects.filter(approved=True)

    return render(request,'ecomadmin/sellerview.html',{'seller_list':sellers})
def sellapprove_page(request):
    sellers = Seller.objects.all()

    return render(request,'ecomadmin/sellapprove.html',{'seller_app':sellers})
def pass_page(request):
    return render(request,'ecomadmin/pass.html')

def approve(request,sid):
    seller=Seller.objects.get(id=sid)
    email = Seller.objects.filter(seller_email = request.session['seller'])
    message = 'you are approved to login'
    send_mail(
        'Login approved',
        message,
        settings.EMAIL_HOST_USER,
        [email,],
        fail_silently=False
    )
    seller.approved=True
    seller.save()
    return redirect('ecome_admin:sellapprove')

def delete_seller(request,sid):
    seller_list = Seller.objects.get(id = sid)
    seller_list.delete()
    return redirect('ecome_admin:sellapprove')
    



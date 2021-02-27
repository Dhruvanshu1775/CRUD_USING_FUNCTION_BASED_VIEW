from django.shortcuts import render,redirect
from .models import customer, product, order
from django.views.generic import UpdateView

from .forms import orderform
from rest_framework import generics
from .serializer import orderserializer
from django.contrib import messages

# Create your views here.

def add_order(request):
    custom = customer.objects.all()
    produc = product.objects.all()

    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        product_name = request.POST['product_name']
        productprice = request.POST['productprice']
        quantity = request.POST['quantity']
        total_price = int(request.POST['productprice'])*int(request.POST['quantity'])
        created = order(customer_name=customer_name,product_name=product_name,productprice=productprice,quantity=quantity,total_price = total_price)
        created.save()
        messages.info(request,f'{customer_name} your order add succesfully')
        return redirect('/')
    else:    
        return render(request,'index.html',{'custom':custom,'produc':produc})



def orderdetail(request):


    help = order.objects.all()
   
    context = {

        'help': help
    }
    return render(request,'customer_info.html',context)

def update(request,id):
    produc = product.objects.all()
    orderty = order.objects.get(id=id)
    if request.method == 'POST':
        form = orderform(request.POST,instance=orderty)
        if form.is_valid():
            form.save()
            return redirect('detail')

    return render(request,'update.html',{'orderty':orderty,'produc':produc})        

def delete(request,id):
    orderty = order.objects.get(id=id)
    orderty.delete() 
    return redirect('/')   


class get(generics.ListAPIView):
    queryset = order.objects.all()
    serializer_class = orderserializer


class post(generics.ListCreateAPIView):
    queryset = order.objects.all()
    serializer_class = orderserializer      
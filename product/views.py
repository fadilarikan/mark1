
from django.contrib.auth.decorators import login_required
from django.db.models.functions import datetime
from django.shortcuts import render, redirect
import os
from django.db import transaction
import warnings

from product.models import Product

warnings.filterwarnings('ignore')

@login_required(login_url="login")
def index(request):
    products = Product.objects.all()
    product_info = []
    for product in products:
        description = {
            'name':product.name,
            'product_id': product.product_id,
            'miad': product.miad,
            'stock': product.stock
        }
        product_info.append(description)
    context= {
        'products':product_info
    }
    return render(request,'index.html',context)

@transaction.atomic
def purchase(request,product_name):
    urun = Product.objects.get(name=product_name)
    urun.purchase = True
    urun.purchase_date = datetime.datetime.now()
    urun.stock -= 1
    urun.save()
    return redirect('index')




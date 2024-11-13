from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import *
import os

# Create your views here.
def shop_login(req):
    if 'shop' in req.session:
        return redirect(shop_home)
    else:
        if req.method=='POST':
            uname=req.POST['uname']
            password=req.POST['password']
            data=authenticate(username=uname,password=password)
            if data:
                login(req,data)
                req.session['shop']=uname
                return redirect(shop_home)
        return render(req,'login.html')
    
def shop_logout(req):
    logout(req)
    req.session.flush()
    return redirect(shop_login)

def shop_home(req):
    if 'shop' in req.session:
        product=Product.objects.all()
        return render(req,'shop/shop_home.html',{'products':product})
    else:
        return redirect(shop_login)
    
def add_product(req):
    if req.method=='POST':
        id=req.POST['pro_id']
        name=req.POST['name']
        discription=req.POST['discription']
        price=req.POST['price']
        offer_price=req.POST['o_price']
        file=req.FILES['img']
        data=Product.objects.create(product_id=id,product_name=name,price=price,offer_price=offer_price,img=file,dis=discription)
        data.save()
        return redirect(shop_home)
    return render(req,'shop/add_product.html')

def edit_product(req,id):
    pro=Product.objects.get(pk=id)
    if req.method=='POST':
        e_id=req.POST['pro_id']
        name=req.POST['name']
        discription=req.POST['discription']
        price=req.POST['price']
        offer_price=req.POST['o_price']
        file=req.FILES.get('img')
        if file:
            Product.objects.filter(pk=id).update(product_id=e_id,product_name=name,price=price,offer_price=offer_price,img=file,dis=discription)
        else:
            Product.objects.filter(pk=id).update(product_id=e_id,product_name=name,price=price,offer_price=offer_price,dis=discription)
        return redirect(shop_home)
    return render(req,'shop/edit_product.html',{'data':pro})


def delete_product(req,id):
    data=Product.objects.get(pk=id)
    url=data.img.url
    url=url.split('/')[-1]
    os.remove('media/'+url)
    data.delete()
    return redirect(shop_home)
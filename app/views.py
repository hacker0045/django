
import json
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from app .models import *
from app.forms import CustomUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
#from django.shortcuts import redirect
#from django.contrib.redirects.models import Redirect
# Create your views here.

def home(request):
       products=Product.objects.filter(trending=1)
       return render(request,"shop/home.html",{"products":products})
 
def logoutpage(request):
  if request.user.is_authenticated:
     logout(request)
  return redirect("/")
 
def card(request):
      if request.user.is_authenticated:
       cart=Card.objects.filter(user=request.user)
       return render(request,"shop/card.html",{"cart":cart})
      else:
       return redirect("/") 
  
def add_card(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_qty=data['product_qty']
      product_id=data['pid']
      #print(request.user.id)
      product_status=Product.objects.get(id=product_id)
      if product_status:
        if Card.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Cart'}, status=200)
        else:
          if product_status.quantity>=product_qty:
            Card.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
            return JsonResponse({'status':'Product Added to Cart'}, status=200)
          else:
            return JsonResponse({'status':'Product Stock Not Available'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Cart'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)
 
 
def loginpage(request):
      if request.user.is_authenticated:
         return redirect("/")
      else:
 
       if request.method=='POST':
         name=request.POST.get('username')
         pwd=request.POST.get('password')
         user=authenticate(request,username=name,password=pwd)
         if user is not None:
           login(request,user)
           messages.success(request,"Logout in Successfully")
           return redirect("/")
         else:
          messages.error(request,"Invalid User Name or Password")
          return redirect("/login")
       return render(request,"shop/login.html")

def register(request):
      form=CustomUserForm()
      if request.method =='POST':
            form=CustomUserForm(request.POST)
            if form.is_valid():
                  form.save()
                  messages.success(request,'registration successful')
                  return redirect('/login')
          
      return render(request,"shop/register.html",{'form':form})

def collections(request):
      catagory=Catagory.objects.filter(status=0)
      return render(request,"shop/collection.html",{"catagory":catagory})
     
def collectionsview(request,name):
  if(Catagory.objects.filter(name=name,status=0)):
      products=Product.objects.filter(category__name=name)
      return render(request,"shop/inc/index.html",{"products":products,"category_name":name})
  else:
    messages.warning(request,"No Such Catagory Found")
    return redirect('collections')
 
 

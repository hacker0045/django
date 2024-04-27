from pyexpat.errors import messages
from django.shortcuts import redirect
from django.shortcuts import render
from app .models import *
#from django.shortcuts import redirect
#from django.contrib.redirects.models import Redirect
# Create your views here.

def home(request):
       products=Product.objects.filter(trending=1)
       return render(request,"shop/home.html",{"products":products})
     
     
def collections(request):
      catagory=Catagory.objects.filter(status=0)
      return render(request,"shop/collection.html",{"catagory":catagory})
     
def collectionsview(request,name):
  if(Catagory.objects.filter(name=name,status=0)):
      products=Product.objects.filter(category__name=name)
      return render(request,"shop/inc/index.html",{"products":products,"category_name":name})
  else:
    return redirect('collections')
  
 

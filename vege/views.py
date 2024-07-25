from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages
# Create your views here.

def receipes(request):
  if request.method=="POST":

   data=request.POST
   receipe_name=data.get('Receipe_name')
   receipe_des=data.get('Receipe_des')
   receipe_image=request.FILES.get('Receipe_img')
   Receipe.objects.create(
     receipe_image=receipe_image,
     receipe_name=receipe_name,
     receipe_description=receipe_des
   )
   return redirect("/receipes/")
 
  
  
  queryset=Receipe.objects.all()
  if request.GET.get('search'):
   queryset= queryset.filter(receipe_name__icontains=request.GET.get('search'))


  context={'receipes':queryset}
  return render(request,"receipes.html",context)



def delete_receipe(request,id):
  queryset=Receipe.objects.get(id=id)
  queryset.delete()
  return redirect('/receipes/')

def update_receipes(request,id):
  queryset=Receipe.objects.get(id=id)
  if request.method=="POST":
   data=request.POST
   receipe_name=data.get('Receipe_name')
   receipe_des=data.get('Receipe_des')
   receipe_image=request.FILES.get('Receipe_img')
   queryset.receipe_name=receipe_name
   queryset.receipe_description=receipe_des
   if receipe_image:
    queryset.receipe_image=receipe_image

   queryset.save()
   return redirect('/receipes/')


   
  context={'receipes':queryset}
  return render(request,'update_receipes.html',context)
  


def login_page(request):
 return render(request,'login.html')






def register_page(request):
 if request.method=="POST":
  first_name=request.POST.get('first_name')
  last_name=request.POST.get('last_name')
  username=request.POST.get('username')
  password=request.POST.get('password')
  user=User.objects.filter(username=username)
  if user.exists():
   messages.info(request, "USername not available")
   return redirect('/register_page/')

  user=User.objects.create(
   first_name=first_name,
   last_name=last_name,
   username=username
   
  )
  messages.info(request, "Account created sucesfully")
  user.set_password(password)
  user.save()
 return render(request,'register.html')
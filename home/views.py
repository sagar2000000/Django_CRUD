from django.shortcuts import render

from django.http import HttpResponse


def home(request):
  peoples=[
    {'name':'sagar joshi','age':20},
    {'name':'rohan dhakal','age':19},
    {'name':'pranaya pradhan','age':15}
  ]
  
  text="hello i am  gggggggggggggg  ggggggggggggggggggggggggggggggggggggggggggggg gggggggggggggggggggggg asagar joshi i a m a vejrhjdh dhdhdhd dhd dhdhdh dhdhdhd dhd dhhddh "
  vegetables=['potato','pumpkin']
  return render(request,"index.html",context={'peoples':peoples ,"text":text,"vegetables":vegetables})
  


def sucess_page(request):
  print("123")
  return HttpResponse( "Hello this is sucess")



def about(request):
  return render(request,"about.html")



def contact(request):
  return render(request,"contact.html")
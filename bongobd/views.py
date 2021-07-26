from django.shortcuts import render
from django.http import HttpResponse
from . models import Myskill,Contactinfo


def home(request):
    
    
    item=Myskill.objects.all()
    title='5 STAR HOTEL IN BANGLADESH'
    desc=' What makes a hotel five-star? A glimpse overview is concerning here...'
    context={
        'title':title,
        'description':desc,
        'data':item
        }
           
   
    return render(request,"index.html",context)


def about(request):
    
    return render(request,"./demo/about.html") 


def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        query=request.POST.get('comments')
        mydata=Contactinfo(cname=name,cemail=email,cquery=query)
        mydata.save()
    return render(request,"contact.html")




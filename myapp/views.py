from django.http import HttpResponse
from django.shortcuts import render
from .models import student

# Create your views here.

def hello_world (request):
    return HttpResponse ("""
    <html>
    <head>
    <title>Learning Django</title>
    </head>
    <body>
    <h1>Heading 1</h1>                                        
    <h2>Heading 2</h2>                    
    <h3>Heading 3</h3>                    
    <h4>Heading 4</h4>                    
    </body>
    </html>                    
                   """)

def hello(request):
    return HttpResponse("<h1>Hello</h1>")

def world(request):
    return HttpResponse("<h2>World</h2>")
def home(request):
    return render(request,template_name='myapp/home.html') 


def protfolio(request):
    return render(request,template_name='myapp/index.html')

def temp_inherit_home(request):

    items = [
        {"name":"shirt","store_location":"KTM","price":900},
        {"name":"ramen","store_location":"BKT","price":150},
        {"name":"crocs","store_location":"PKR","price":1200},
    ]
    return render(request,template_name='myapp/temp_inherit_home.html',context= {"name":"bvk","age":24,"address":"KTM","items":items})


def temp_inherit_features(request):
    items = [
        {"name":"mobile","store_location":"KTM","price":1250},
        {"name":"kitkat","store_location":"BKT","price":150},
        {"name":"pen","store_location":"PKR","price":15},
    ]
    return render(request,template_name='myapp/temp_inherit_features.html',context = {"items":items})

def temp_inherit_pricing(request):
    students = student.objects.all()
    return render(request,template_name='myapp/temp_inherit_pricing.html',context = {"students": students})


from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
def index(request):
    return render(request,"index.html", {
    "message": "Listado de productos",
    "title": "Productos",
    "products": [
        {"title" : "Playera", "price" : 5, "stock" : True},
        {"title" : "Camisa", "price" : 7, "stock" : True},
        {"title" : "Mochila", "price" : 20, "stock" :False},
        {"title" : "Laptop", "price" : 500, "stock" :True},
    ]

    })

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username") #diccionario
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)
        if user:
            login(request,user)
            return redirect("index")
    return render(request, "users/login.html")
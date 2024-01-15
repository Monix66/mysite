from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

def index(request):
    return HttpResponse("Hello, <b>world</b>. You're at the polls index.")

def llista(request):
    items = User.objects.all()
    return render( request, "llista.html",
        {
            "tipus":"coses",
            "elements":items
        }
    )          

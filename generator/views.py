from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, "generator/home.html")

def information(request):
    return render(request, "generator/information.html")

def password(request):

    characters = list("abcdefghijklmnoprstuvwxyz")

    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPRTUVWXYZ"))
    
    if request.GET.get("special"):
        characters.extend(list("!@#$%^&*()"))

    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))

    lenght = int(request.GET.get("lenght"))

    thepassword = ""
    for x in range(lenght):
        thepassword+= random.choice(characters)


    return render(request, "generator/password.html", {"password": thepassword})

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(response):
    return HttpResponse("<h1>Hello My World</h1>")

def v1(response):
    return HttpResponse("<h1>F... the rest of the W!</h1>")

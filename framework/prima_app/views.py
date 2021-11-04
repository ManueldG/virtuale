from django.shortcuts import render

from django.http import HttpResponse

def homepage(request):
    print(request)
    return HttpResponse('<h1>ciao!!!!</h1>')


from django.shortcuts import render
# from django.http import HttpResponse

def first(request):
    return render(request,"first.html")

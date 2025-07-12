from django.shortcuts import render
# Create your views here
# from django.http import HttpResponse
from blog.models import Stories
from math import ceil
def bloghome(request):
    return render(request,"bloghome.html")
    # return HttpResponse("We are home page of blog")



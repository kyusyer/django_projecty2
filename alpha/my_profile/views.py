from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"my_profile/index.html")

def project(request):
    return render(request, "my_profile/project.html")
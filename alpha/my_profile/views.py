from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django import forms


class NewTaskForm(forms.Form):
    name = forms.CharField(label="New Project")
    desc = forms.CharField(label="Description")
    link = forms.CharField(label="Link")

    
projects = [
    {
        "name": "Morse Code:Encoder Decoder",
        "desc": "A program written in python that converts alphaneumeric characters into morse code\
              or convert morse code into alphanumeric characters",
        "link": "https://github.com/kyusyer/morsecode"
    },
    {
        "name": "Fullstack website using django",
        "desc": "A full stack website that contains my resume that is written in django",
        "link": "https://github.com/kyusyer/django_projecty2"
    }
]


# Create your views here.

def index(request):
    return render(request,"my_profile/index.html")

def project(request):
    return render(request, "my_profile/project.html", {
        "projects": projects
    })


def add_project(request): 
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            desc = form.cleaned_data["desc"]
            link = form.cleaned_data["link"]
            projects.append(
                {
                    "name": name,
                    "desc": desc,
                    "link": link
                }
            )
            return HttpResponseRedirect(reverse("my_profile:project"))

    return render(request, "my_profile/add_project.html", {"form": NewTaskForm()} )

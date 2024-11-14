from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from main.models import Contact 
from projects.models import Project 

# Create your views here.


def dashboard_view(request:HttpRequest):
    contact = Contact.objects.all()
    project = Project.objects.all()

    if 'data' in request.POST:
        if request.POST["data"] == "messages":
            return render(request,"dashboard/dashboard.html" , {"contact":contact})
        elif request.POST["data"] == "projects":
            return render(request,"dashboard/dashboard.html" , {"project":project})

    return render(request,"dashboard/dashboard.html" , {"contact":contact,"project":project})
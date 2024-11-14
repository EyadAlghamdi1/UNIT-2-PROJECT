from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from main.models import Contact 
from projects.models import Project 

# Create your views here.


def dashboard_view(request:HttpRequest):
    contact = Contact.objects.all()
    project = Project.objects.all()
    return render(request,"dashboard/dashboard.html" , {"contact":contact},{"project":project} )
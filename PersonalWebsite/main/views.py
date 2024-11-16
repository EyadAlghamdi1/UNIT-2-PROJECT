from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from .models import Contact
from projects.models import Project
# Create your views here.

def home_view(request:HttpRequest):
    projects = Project.objects.all()[:3]
    return render(request,"main/home.html",{"projects":projects})

def about_view(request:HttpRequest):
    return render(request,"main/about.html")

def skills_view(request:HttpRequest):
    return render(request,"main/skills.html")


def contact_view(request: HttpRequest):
    if request.method == "POST":
        user_message = Contact(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
            message=request.POST["message"],
        )
        user_message.save()
    return render(request, "main/contact.html")

def message_detail_view(request: HttpRequest,message_id:int):
    user_message = Contact.objects.get(pk=message_id)  
    return render(request, "main/message_detail.html", {"user_message": user_message})


def delete_view(request:HttpRequest,message_id:int):
    user_message = Contact.objects.get(pk=message_id)
    user_message.delete()
    return redirect("dashboard:dashboard_view")

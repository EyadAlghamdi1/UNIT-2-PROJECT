from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from .models import Contact , Skill
from projects.models import Project
# Create your views here.

def home_view(request:HttpRequest):
    projects = Project.objects.all()[:3]
    return render(request,"main/home.html",{"projects":projects})

def about_view(request:HttpRequest):
    return render(request,"main/about.html")

def skills_view(request: HttpRequest):
    skills_by_category = {
        'Front End': Skill.objects.filter(category="Front End"),
        'Back End': Skill.objects.filter(category="Back End"),
        'Tool': Skill.objects.filter(category="Tool"),
    }
    return render(request, "main/skills.html", {"skills_by_category": skills_by_category})

def add_skill_view(request: HttpRequest):
    if request.method == "POST":
        skill = Skill(
            name=request.POST["name"],
            icon=request.FILES["icon"],
            category=request.POST["category"],
        )
        skill.save()      
    return render(request, "main/add_skill.html")

def delete_skill_view(request:HttpRequest,skill_id:int):
    skill = Skill.objects.get(pk=skill_id)
    skill.delete()
    return redirect("dashboard:dashboard_view")


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

from django.shortcuts import render ,redirect
from django.http import HttpRequest,HttpResponse
from .models import Project
# Create your views here.
 

def projects_view(request:HttpRequest):
    projects = Project.objects.all()
    return render(request,"projects/projects.html" , {"projects": projects})


def add_projects_view(request: HttpRequest):
    if request.method == "POST":
        new_project = Project(
            title=request.POST["title"],
            description=request.POST["description"],
            image=request.FILES["image"],
            category=request.POST["category"],
            tools=request.POST["tools"], 
            live_url=request.POST["live_url"],  
            github_url=request.POST["github_url"],
            status=request.POST["status"]
        )
        
        new_project.save()
        
        return redirect("projects:projects_view")  

    return render(request, "projects/add_project.html")


def detail_view(request:HttpRequest,project_id:int):
    project_detail = Project.objects.get(pk=project_id)
    return render(request,"projects/detail.html",{"project_detail":project_detail})

def update_view(request:HttpRequest,project_id:int):
    project_detail = Project.objects.get(pk=project_id)
    if request.method == "POST":
        project_detail.title = request.POST["title"]
        project_detail.description = request.POST["description"]
        project_detail.image = request.FILES["image"]
        project_detail.category = request.POST["category"]
        project_detail.status = request.POST["status"]
        project_detail.tools = request.POST["tools"]
        project_detail.live_url = request.POST["live_url"]
        project_detail.github_url = request.POST["github_url"]
        project_detail.save()
        return redirect("dashboard:dashboard_view")

    return render(request,"projects/update.html", {"project_detail":project_detail})


def delete_view(request:HttpRequest,project_id:int):
    project_detail = Project.objects.get(pk=project_id)
    project_detail.delete()
    return redirect("dashboard:dashboard_view")



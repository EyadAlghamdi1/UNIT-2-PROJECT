from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from main.models import Contact ,Skill
from projects.models import Project 

# Create your views here.


def dashboard_view(request:HttpRequest):
    contact = Contact.objects.all()
    project = Project.objects.all()
    skill =   Skill.objects.all()
    data_filter = request.POST.get('data') or request.GET.get('data', 'all')
    sort_option = request.GET.get('sort')

    if data_filter == "messages":
        project, skill = None, None  
        if sort_option == 'newest':
            contact = contact.order_by('-id')
        elif sort_option == 'oldest':
            contact = contact.order_by('id')

    elif data_filter == "projects":
        contact, skill = None, None
        if sort_option == 'newest':
            project = project.order_by('-id')
        elif sort_option == 'oldest':
            project = project.order_by('id')

    elif data_filter == "skills":
        contact, project = None, None
        if sort_option == 'newest':
            skill = skill.order_by('-id')
        elif sort_option == 'oldest':
            skill = skill.order_by('id')


    return render(request, "dashboard/dashboard.html", {
            "contact": contact,
            "project": project,
            "skill": skill,
            "data_filter": data_filter,
            "sort_option": sort_option  
        })
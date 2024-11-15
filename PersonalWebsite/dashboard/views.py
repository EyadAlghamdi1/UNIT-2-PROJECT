from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from main.models import Contact 
from projects.models import Project 

# Create your views here.


def dashboard_view(request:HttpRequest):
    contact = Contact.objects.all()
    project = Project.objects.all()
    data_filter = request.POST.get('data', 'all')  

    sort_option = request.GET.get('sort')
    if data_filter == "messages":
        project = None  
        if sort_option == 'newest':
            contact = contact.order_by('-created_at')
        elif sort_option == 'oldest':
            contact = contact.order_by('created_at')
    elif data_filter == "projects":
        contact = None  
        if sort_option == 'newest':
            project = project.order_by('-created_at')
        elif sort_option == 'oldest':
            project = project.order_by('created_at')

    return render(request, "dashboard/dashboard.html", {
        "contact": contact,
        "project": project,
        "data_filter": data_filter
    })
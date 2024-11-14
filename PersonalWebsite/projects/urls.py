from django.urls import path 
from . import views

app_name = "projects"

urlpatterns = [
    path('projects/',views.projects_view,name="projects_view"),  
    path('add/',views.add_projects_view,name="add_projects_view"),
    path('update/<project_id>',views.update_view,name="update_view"),
    path('delete/<project_id>',views.delete_view,name="delete_view"),
    path('detail/<project_id>',views.detail_view,name="detail_view"),
]
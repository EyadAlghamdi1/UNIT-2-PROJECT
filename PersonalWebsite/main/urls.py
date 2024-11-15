from django.urls import path 
from . import views

app_name = "main"

urlpatterns = [
    path('',views.home_view,name="home_view"),  
    path('contact/',views.contact_view,name="contact_view"),
    path('detail/<message_id>',views.message_detail_view,name="message_detail_view"), 
    path('delete/<message_id>',views.delete_view,name="delete_view"), 
    path('about',views.about_view,name="about_view"), 
]
from django.urls import path
from django.views.generic import TemplateView
from .views import homepage,about,resume,projects,experiences,certification,contact,resume_download,services

urlpatterns = [
    path('',homepage,name='index'),
    path('about/',about,name='about'),
    path('projects/',projects,name='projects'),
    path('experiences/',experiences,name='experiences'),
    path('certification/',certification,name='certification'),
    path('contact/',contact, name='contact'),
    path('resume/',resume, name='resume'),
    path('resume/download',resume_download, name='download_resume'),
    path('services/',services,name='services'),
    path('success/',TemplateView.as_view(template_name='success.html'),name='success'),
    # path('send_message/',send_message,name='send_message'),
]

from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from .forms import MessageForm
from .models import Message
import requests
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


#homepage

def homepage(request):
    return render(request,'homepage.html')
def about(request):
    return render(request,'about.html')
def projects(request):
    projects_show = [
        {"title":"Library Management API",
         "image_path":"images/libraryapi.png",
         "link":"https://github.com/Guandaru-Kabugi/Capstone-Project-Library-Management-API"},
        
        {"title":"Personal Orders API",
         "image_path":"images/personalorders.png",
         "link":"https://github.com/Guandaru-Kabugi/orderproject"},
        
        {"title":"Blogpost Project",
         "image_path":"images/blogpost.png",
         "link":"https://github.com/Guandaru-Kabugi/blog-project"},
        
        {"title":"Portfolio Project",
         "image_path":"images/portfolio.png",
         "link":"https://github.com/Guandaru-Kabugi/Portfolio"},
        
        {"title":"Social Media API",
         "image_path":"images/socialmedia.png",
         "link":"https://github.com/Guandaru-Kabugi/Social-Media-Api"}
    ]
    return render(request,'projects.html',{"projects_show":projects_show})
def experiences(request):
    experiences = [
        {"company":"ALX Africa",
         "position":"Student",
         "start_date":"2024-03-21",
         "end_date":"2024-10-31"
        },
        
        
    ]
    return render(request,'experiences.html',{"experiences":experiences})
def certification(request):
    certificates = {"name":"Backend Web Development Certificate",
         "issuer":"ALX Africa",
         "issue_date":"2024-10-31",
        },
    return render(request,'certification.html',{"certificates":certificates})
# def contact(request):
#     return render(request,'contact.html')
def resume(request):
    return render(request, "resume.html")
def resume_download(request):
    resume_path = "docs/Guandaru_Kabugi_Resume.pdf"
    resume_path = staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response["Content-Disposition"]='attachment';filename="Guandaru_Kabugi_Resume.pdf"
            return response
    else:
        return HttpResponse("resume not found", status=404)
def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()  # save data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient_list = ['guandarualex3@gmail.com']  

            # Message content for the email
            
            message_content = {
                "Sender":name,
                "Sender_Email":email,
                "Message_Subject":subject,
                "Message":message
            }

            # Send email using Mailgun API
            response = requests.post(
                f"https://api.mailgun.net/v3/{settings.MAILGUN_DOMAIN}/messages",
                auth=("api", settings.MAILGUN_API_KEY),
                data={
                    "from": f"Alex Kabugi <mailgun@{settings.MAILGUN_DOMAIN}>",  # Adjust this as needed
                    "to": recipient_list,
                    "subject": subject,
                    "text": JsonResponse(message_content)
                }
            )

            # Debugging with print
            print("Response Status Code:", response.status_code)
            print("Response Text:", response.text)

            # Check if email was sent successfully
            if response.status_code == 200:
                return redirect('success')  # Redirect to a success page if the email is sent
            else:
                return render(request, 'contact.html', {'form': form, 'error': 'Failed to send email. Please try again later.'})
    else:
        form = MessageForm()
    
    return render(request, 'contact.html', {"form": form})
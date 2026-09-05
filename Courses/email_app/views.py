from django.shortcuts import render
from django.conf import settings 
from django.http import HttpResponse 
from django.core.mail import send_mail 

def send_email(request):
    send_mail(
        subject = "Test Email from Django", 
        message = "Hello, this email is sent using Django.", 
        from_email = "pmaheshwari.8125@gmail.com", 
        recipient_list = ["maheshwaripeddapirangiemail@gmail.com"], 
        fail_silently=False
        )
    return HttpResponse("Email sent successfully")
    

# Create your views here.

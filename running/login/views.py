from django.shortcuts import render
from django.http import HttpResponse
def home(req):
    return render(req,'home.html',{'name':'Maheshwari'})
def login(req):
    user=req.POST.get("username")
    pas=req.POST.get("password")
    return render(req,"login.html",{'username':user,'password':pas})


# Create your views here.

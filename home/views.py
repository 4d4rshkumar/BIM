from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.

def index(req):
    #return HttpResponse("this is homepage")
    return render(req,"index.html")


def search(req):
    #return HttpResponse("this is homepage")
    return render(req, "finder.html")
def about(req):
    return render(req, "about.html")
def contact(req):
    if req.method=="POST":
        name=req.POST.get("name")
        mail=req.POST.get("mail")
        number=req.POST.get("number")
        desc = req.POST.get("desc")
        contact=Contact(name=name,mail=mail,number=number,desc=desc,date=datetime.today())
        contact.save()
        messages.success(req, 'Message Sent!')
    return render(req, "contact.html")

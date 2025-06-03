from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        'variable1': "this is sent1",
        'variable2': "this is sent2",
        'variable3': "this is sent3"
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")
    
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject, message=message, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent successfully!")
        
    return render(request, "contact.html")
from django.shortcuts import render, HttpResponse

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
    return render(request, "contact.html")
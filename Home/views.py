from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime
from Home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("This is Home")

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        decs = request.POST.get('decs')
        contact = Contact(name=name, email=email, phone=phone, address=address, decs=decs, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')

    return render(request, 'contact.html')

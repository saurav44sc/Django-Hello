from datetime import datetime
import re
from django.shortcuts import render, HttpResponse

from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'variable1': "this is a variable",
        'variable2': "this is another variable"
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        date = datetime.today()
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=date)
        contact.save()
        messages.success(request, 'New contact added successfully')

    return render(request, 'contact.html')

import imp
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from django.contrib import messages
from django.http import HttpResponseRedirect


# Fuction to render the Home Page
def frontend(request):
    return render(request, "frontend.html")


# Fuction to render the Backend Page
@login_required(login_url="login")
def backend(request):
    return render(request, "backend.html")


# Fuction to insert patient
@login_required(login_url="login")
def add_patient(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('age') and request.POST.get('gender') and request.POST.get('note'):
            patient = Patient()
            patient.name = request.POST.get('name')
            patient.phone = request.POST.get('phone')
            patient.email = request.POST.get('email')
            patient.age = request.POST.get('age')
            patient.gender = request.POST.get('gender')
            patient.note = request.POST.get('note')
            patient.save()
            messages.success(request, "Patient added successfully!")
            return HttpResponseRedirect('/backend')
    else:
        return render(request, "add.html")

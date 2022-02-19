import imp
from unicodedata import name
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator


# Fuction to render the Home Page
def frontend(request):
    return render(request, "frontend.html")


# Fuction to render the Backend Page
@login_required(login_url="login")
def backend(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_patient_list = Patient.objects.filter(
            Q(name__icontains=q) | Q(phone=q) | Q(
                email=q) | Q(age=q) | Q(gender=q) | Q(note=q)
        ).order_by('-created_at')
    else:
        all_patient_list = Patient.objects.all().order_by('-created_at')

    paginator = Paginator(all_patient_list, 10)
    page = request.GET.get('page')
    all_patient = paginator.get_page(page)

    return render(request, 'backend.html', {
        "patients": all_patient
    })


# Fuction to insert patient
@login_required(login_url="login")
def add_patient(request):
    if request.method == "POST":
        if request.POST.get('name') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('age') and request.POST.get('gender') or request.POST.get('note'):
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


# Fuction to delete patient
@login_required(login_url="login")
def delete_patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    patient.delete()
    messages.success(request, "Patient removed successfully!")
    return HttpResponseRedirect('/backend')


# Fuction to access the patient individually
@login_required(login_url="login")
def patient(request, patient_id):
    patient = Patient.objects.get(id=patient_id)
    if patient != None:
        return render(request, "edit.html", {'patient': patient})

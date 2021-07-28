from django.shortcuts import render, HttpResponseRedirect
from .forms import PatientRegistration
from .models import user


# Create your views here.

# this for add
def add_show(request):
    if request.method == 'POST':
        fm = PatientRegistration(request.POST)
        if fm.is_valid():
            bn = fm.cleaned_data['Patient_name']
            ba = fm.cleaned_data['Patient_address']
            bc = fm.cleaned_data['Phone_No']
            reg = user(Patient_name=bn, Patient_address=ba, Phone_No=bc)
            reg.save()
            fm = PatientRegistration()
    else:
        fm = PatientRegistration()
    Patient = user.objects.all()
    return render(request, 'addandshow.html', {'form': fm, 'stu': Patient})


def update_data(request, id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        fm = PatientRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = user.objects.get(pk=id)
        fm = PatientRegistration(instance=pi)
    return render(request, 'update.html', {'form': fm})


# this is for delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

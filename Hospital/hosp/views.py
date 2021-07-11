from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"home.html")
def specialists(request):
    return render(request,"specialists.html")
def contact(request):
    return render(request,"contact.html")
def appointment(request):
    return render(request,"appointment.html")

from django.shortcuts import render

# Create your views here.
def swing(request):
    return render(request,"home.html")

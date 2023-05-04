from django.shortcuts import render

def home(request):
    return render(request, 'home/homepage.html')
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def mainpage(request):
    return render(request, 'initpage/initpage.html')
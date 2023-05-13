from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.http import HttpResponse
from login.forms import UserForm

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password) 
            login(request, user)
            return redirect('http://127.0.0.1:8000/userlogin/auth/')
    else:
        form = UserForm()
    return render(request, 'login/signup.html', {'form': form})

# 구글 로그인 API 연결

from social_core.exceptions import AuthAlreadyAssociated

def auth_allowed(backend, uid, user=None, *args, **kwargs):
    print("backend >>", backend)
    print("uid >> ",  uid)
    print("user >> ",  user)
    print("args >> ",  args)
    print("kwargs >> ",  kwargs)
    
    return redirect('http://127.0.0.1:8000/main/homepage/')
    # return HttpResponse("로그인 성공")
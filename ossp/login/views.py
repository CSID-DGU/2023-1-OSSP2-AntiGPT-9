from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import MyUserCreationForm, MyUserChangeForm, MyAuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('http://127.0.0.1:8000/userlogin/auth/')
    else:
        form = MyUserCreationForm()
    return render(request, 'login/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = MyAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('http://127.0.0.1:8000/main/homepage/')
            else:
                form.add_error(None, 'Invalid email or password.')
    else:
        form = MyAuthenticationForm()
    return render(request, 'login/login.html', {'form': form})
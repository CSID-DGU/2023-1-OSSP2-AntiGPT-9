from django.shortcuts import render, redirect
from django.urls import reverse
from django.core import signing
from home.views import get_encrypted_url
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import MyUserCreationForm, MyUserChangeForm, MyAuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login:login')
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
                url = reverse('homepage:homepage',args=[user.id])
                return redirect(reverse('homepage:process') + get_encrypted_url(url))
            else:
                form.add_error(None, 'Invalid email or password.')
    else:
        form = MyAuthenticationForm()
    return render(request, 'login/login.html', {'form': form})

def auth_allowed( backend, uid, user=None, *args, **kwargs):
    
    print("backend >>", backend)
    print("uid >> ",  uid)
    print("user >> ",  user)
    print("args >> ",  args)
    print("kwargs >> ",  kwargs)
    
    url = reverse('homepage:homepage',args=[user.id])
    return redirect(reverse('homepage:process') + get_encrypted_url(url))

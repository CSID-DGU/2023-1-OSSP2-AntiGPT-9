from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "login"
urlpatterns = [
    path('main/', views.mainpage),
    path('auth/', auth_views.LoginView.as_view(template_name = 'login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login/newvbar.html'), name='logout'),
    path('signup/', views.signup, name='signup'),
]
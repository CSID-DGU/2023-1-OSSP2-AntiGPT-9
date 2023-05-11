from django.urls import path, re_path
from . import views

app_name = 'initpage'
urlpatterns = [
    path('homepage/', views.home, name='homepage')
]

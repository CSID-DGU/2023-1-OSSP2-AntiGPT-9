from django.urls import path, re_path
from . import views

app_name = 'initpage'
urlpatterns = [
    path('', views.mainpage, name='initpage')
]
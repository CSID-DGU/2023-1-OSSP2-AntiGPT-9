from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "login"
urlpatterns = [
    path('main/', views.mainpage),
    path('auth/', auth_views.LoginView.as_view(template_name = 'login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login/newvbar.html'), name='logout'),
    # 수정해야하는 코드
    # django.contrib.auth앱의 LoginView 클래스를 활용했으므로 별도의 views.py 파일 수정이 필요 없음
]
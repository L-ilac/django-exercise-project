from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.main_login_view, name="main_login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register_view, name="register"),
    path('mypage/', views.mypage_view, name="mypage"),

    # path('mypage/', views.mypage_view,name="mypage"),


]

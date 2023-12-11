from apps.LoginRegister import views
from django.urls import path

urlpatterns = [
    path('login/',views.showlogin)
]
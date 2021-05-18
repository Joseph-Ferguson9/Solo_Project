from django.urls import path
from . import views

urlpatterns = [
    path('page/login', views.page_login),
    path('page/register', views.page_register),
    path('user/register', views.register),
    path('user/login', views.login),
    path('user/logout', views.logout),
]
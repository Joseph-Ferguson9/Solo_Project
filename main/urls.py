from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('user/dash', views.user_dash),
    path('user/edit_profile', views.edit_profile),
]
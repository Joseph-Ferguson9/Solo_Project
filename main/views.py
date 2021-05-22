from django.shortcuts import render, redirect
from django.contrib import messages
from login.models import Users

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def user_dash(request):
    context = {
        'logged_user': Users.objects.get(id=request.session["logged_user"]),
    }
    return render(request, 'dashboard.html', context)

def new_post(request):
    return render(request, 'new_post.html')

def edit_profile(request):
    context = {
        'logged_user': Users.objects.get(id=request.session['logged_user']),
    }
    return render(request, 'edit_profile.html', context)
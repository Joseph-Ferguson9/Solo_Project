from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Users
import bcrypt

# Create your views here.
def page_login(request):
    return render(request, 'login.html')

def page_register(request):
    return render(request, 'register.html')

def register(request):
    errors = Users.objects.user_validator(request.POST)
    if request.method == 'POST':
        if errors:
            for value in errors.items():
                messages.error(request, value)
            return redirect('/')
        hash_pw = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = Users.objects.create(
            f_name=request.POST['f_name'],
            l_name=request.POST['l_name'],
            email=request.POST['email'],
            bday=request.POST['bday'],
            password=hash_pw
        )
        request.session['logged_user'] = new_user.id
        return redirect('/user/edit_profile')
    return redirect('/login/page/register')


def login(request):
    if request.method == 'POST':
        user = Users.objects.filter(email=request.POST['email'])
        # Use filter over get because if there is no email that matches request.POST an error will occur, filter does not do this
        if user:  # saying if there is a user, boolean
            log_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):
                # compares the Posted password to the one stored within the database
                # Puts the logged in user to session, only if the password is correct.
                request.session['logged_user'] = log_user.id
                return redirect('/user/dash')
                # localhost:8000/user/dashboard
        messages.error(request, "Email or password are incorrect")
    return redirect('/login/page/login')


def logout(request):
    request.session.flush()
    return redirect('/')

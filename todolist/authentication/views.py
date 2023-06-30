from django.views.generic import View
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.conf import settings
from .form import LoginForm,Sign_up

def signup(request):
    form =Sign_up()
    message='not'
    if request.method=="POST":
        form = Sign_up(request.POST)
        if form.is_valid():
            newUser = form.save()
            message="yes"
            login(request,newUser)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render (request,'authentication/sign_up.html',context={'form':form,"message":message})

def login_page(request):
    form = LoginForm()
    message = 'l'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
                return redirect("Todos")

            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'authentication/login.html', context={'form': form, 'message': message})


def logout_user(request):    
    logout(request)
    return redirect('login')
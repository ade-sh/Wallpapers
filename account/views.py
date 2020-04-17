from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
import logging
from django.contrib.auth.decorators import login_required
from .models import SignUpForm
logger = logging.getLogger(__name__)


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('account')
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email= form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password, email=email)
            login(request, user)
            return redirect('/accounts')
        else:
            return render(request, template_name='account/signup.html', context={'form': form})
    else:
        form=SignUpForm()
        return render(request, template_name='account/signup.html', context={'form': form})


def login_form(request):
    if request.user.is_authenticated:
        return redirect('account')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            logger.info('login successful')
            return redirect('/accounts')
        else:
            return render(request, template_name='account/login.html',context={"error_message": "Login Failed"})
    else:
        return render(request, template_name='account/login.html')


@login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        user = request.user
    return render(request, template_name='account/account.html', context={'username': user.username})


def logout_user(request):
    logout(request)
    return render(request, template_name='account/login.html',context={"success_message": "Logged out successfully "})

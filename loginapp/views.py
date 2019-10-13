from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.contrib import messages

from .forms import UserUpdateForm, ProfileUpdateForm
from .utils import random_string


def login(request):
    context = {}
    if request.method == 'POST':
        user = authenticate(request, 
            username=request.POST['user'], 
            password=request.POST['password'])
        if user:
            dj_login(request, user)
            # is this just stupid? context = {'user':request.POST['user']}
            return HttpResponseRedirect(reverse('shop:product_list'))
        else:
            #context = {'error':'Username or password is wrong.'}
            context['error'] = 'Username or password is wrong.'

    return render(request, 'loginapp/login.html', context)

def logout(request):
    dj_logout(request)
    return HttpResponseRedirect(reverse('loginapp:login'))

def signup(request):
    if User.is_authenticated:
        dj_logout(request)
    context = {}
    if request.method == 'POST':
        if not request.POST['password'] == request.POST['repeatpassword']:
            context['error'] = 'Passwords do not match.'
            return render(request, 'loginapp/signup.html', context)
        if len(User.objects.filter(username=request.POST['user'])) > 0:
            context['error'] = 'Username already exists.'
            return render(request, 'loginapp/signup.html', context)
        user = User.objects.create_user(request.POST['user'],password=request.POST['password'])
        user.save()
        dj_login(request, user)
        return HttpResponseRedirect(reverse('shop:product_list'))

    return render(request, 'loginapp/signup.html')

def password_reset(request):
    context = {}
    if request.method == 'POST':
        users = User.objects.filter(username=request.POST['user'])
        if users:
            user = users[0]
            new_password = random_string()
            user.set_password(new_password)
            user.save()
            print(f'**** User {user} change password to {new_password}')
            return HttpResponseRedirect(reverse('loginapp:login'))
        else:
            context['error'] = 'No such username.'
        
    return render(request, 'loginapp/password_reset.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return HttpResponseRedirect(reverse('loginapp:profile'))
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'loginapp/profile.html', context)
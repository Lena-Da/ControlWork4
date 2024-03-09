from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import *


@login_required(login_url='login')
def account_home(request):
    return render(request, 'account/account_home.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('account_home')
    else:
        error = ''
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()

                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)

                login(request, user)
                return redirect('account_home')
            else:
                error = 'Неправильно введенные данные'

        data = {
            'form': form,
            'error': error
        }

        return render(request, 'account/register.html', data)


def login_acc(request):
    if request.user.is_authenticated:
        return redirect('account_home')
    else:
        error = ''
        form = Authenticate()

        if request.method == 'POST':
            form = Authenticate(data=request.POST)

            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')

                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('account_home')
            else:
                error = 'Неправильно введенные данные'
        data = {
            'form': form,
            'error': error,
        }

    return render(request, 'account/login.html', data)


@login_required(login_url='login')
def logout_acc(request):
    if request.user.is_authenticated:
        logout(request)

        return redirect('home')

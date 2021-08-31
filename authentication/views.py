from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login


def login(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        form = LoginForm(request.POST)
        message = "Hata oluştu tekrar deneyiniz"
        if form.is_valid():
            username = form.cleaned_data.get("name")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                return render(request, 'login.html', {"form": form, "message": message})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def register_request(request):
    message = " "
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password1 = form.cleaned_data.get("password1")
            password2 = form.cleaned_data.get("password2")
            email = form.cleaned_data.get("email")
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    message= 'Username taken,please use different username.'
                elif User.objects.filter(email=email).exists():
                    message = 'Email is taken,please use different email.'
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
            else:
                message= 'Passwords are not matching, please check them.'

            return redirect('login')
    else:
        form = NewUserForm()

    return render(request,"register.html",{"form": form,'message':message})

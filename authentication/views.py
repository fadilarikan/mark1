from django.shortcuts import render, redirect
from .forms import LoginForm
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
            user = authenticate(username=username,password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('index')
            else:
                return render(request,'login.html',{"form":form,"message":message})
    else:
        form = LoginForm()

    return render(request, 'login.html',{'form':form})



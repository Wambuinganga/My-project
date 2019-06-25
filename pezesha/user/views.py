from django.shortcuts import render
from .forms import UserForm, LoginForm, UpdateForm

def register_user(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=UserForm()
    return render(request, "register_user.html",{"form":form})

def login(request):
    
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=UserForm()
    return render(request, "login.html",{"form":form})

def user_update(request):
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=UserForm()
    return render(request, "user_update.html",{"form":form})

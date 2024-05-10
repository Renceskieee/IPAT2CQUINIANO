from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import Record

# Create your views here.

def main(request):
    #what you want to do

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['user_password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In!")
            return redirect('main')
        else:
            messages.success(request, "Invalid Account, Please Try Again...")
            return redirect('main')
    else:

        return  render(request, 'main.html')

def members(request):
    #what you want to do

    records = Record.objects.all()

    return  render(request, 'members.html', {'members':records})

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Account Created!")
            return redirect('main')
    else:
        form = SignUpForm
        return render(request,'register.html',{'form':form})
    
    return render(request,'register.html',{'form':form})

def logout_user(request):
    logout(request)
    messages.success(request, "Account has been Logged Out!")
    return redirect('main')
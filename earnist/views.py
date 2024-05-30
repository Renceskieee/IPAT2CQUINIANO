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
            messages.success(request, "Invalid, Please Try Again...")
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
            return redirect('register')
    else:
        form = SignUpForm
        return render(request,'register.html',{'form':form})
    
    return render(request,'register.html',{'form':form})

def add_record(request):
    forms = AddRecordForm(request.POST or None)
    if  request.user.is_authenticated:
        if request.method == 'POST':
            add_record = forms.save()
            messages.success(request, "New Member Added!")
            return redirect('members')
        return render(request, "add.html", {'forms':forms})
    else:
         messages.success(request, "Invalid Action...")
         return redirect('main')

def update_record(request, pk):
    if  request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record )
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Updated!")
            return redirect('members')
        return render(request, "update.html", {'form':form})

    else:
         messages.success(request, "Invalid Action...")
         return redirect('main')

def delete_record(request, pk):
    if  request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "Member Has Been Removed!")
        return redirect('members')

    else:
         messages.success(request, "Invalid Action...")
         return redirect('main')

def logout_user(request):
    logout(request)
    messages.success(request, "Account has been Logged Out!")
    return redirect('main')
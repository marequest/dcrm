from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Record
from .forms import AddRecordForm

# Create your views here.

def home(request):
    records = Record.objects.all()

    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.success(request, 'Invalid username or password')
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('home')


def customer_record(request, pk):
    if request.user.is_authenticated:
        # look up that record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, 'You must be logged in')
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        # look up that record
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, f"Deleted record {delete_record.first_name} {delete_record.last_name} successfully")
        return redirect('home')
    else:
        messages.success(request, 'You must be logged in')
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record successfully added')
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, 'You must be logged in')
        return redirect('home')


def edit_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record successfully updated')
            return redirect('home')
        return render(request, 'edit_record.html', {'form': form})
    messages.success(request, 'You must be logged in')
    return redirect('home')

from django.shortcuts import render


from django.shortcuts import render

from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .forms import fileform, registerform
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.files.storage import FileSystemStorage


@login_required(login_url='login-page')
def manager(request):
    mangfile = filesend.objects.filter(Department='Manager')

    mancomplete = filesend.objects.filter(Status='Complete',Department='Manager').count()

    manprogress = filesend.objects.filter(Status='On-progress',Department='Manager').count()

    mantotal_projectsmag = filesend.objects.filter(Department='Manager').count()

    manpending = filesend.objects.filter(Status='Pending',Department='Manager').count()
    context = {'mangfile': mangfile, 'total_projectsmag': mantotal_projectsmag, 'mancomplete': mancomplete, 'manprogress': manprogress,
               'manpending': manpending}
    return render(request, 'manager.html', context)


@login_required(login_url='login-page')
def employer(request):
    empfile = filesend.objects.filter(Department='Employer')

    complete = filesend.objects.filter(Status='Complete',Department='Employer').count()

    progress = filesend.objects.filter(Status='On-progress',Department='Employer').count()

    total_projectsemp = filesend.objects.filter(Department='Employer').count()

    pending = filesend.objects.filter(Status='Pending',Department='Employer').count()
    context = {'empfile': empfile, 'total_projectsemp': total_projectsemp, 'complete': complete, 'progress': progress,
               'pending': pending}
    return render(request, 'emppage.html', context)


@login_required(login_url='login-page')
def teamleader(request):
    totfile = filesend.objects.all()

    complete = filesend.objects.filter(Status='Complete').count()

    progress = filesend.objects.filter(Status='On-progress').count()

    total_projects = filesend.objects.count()

    pending = filesend.objects.filter(Status='Pending').count()
    context = {'totfile': totfile, 'total_projects': total_projects, 'complete': complete, 'progress': progress,
               'pending': pending}
    return render(request, 'tlpage.html', context)


@login_required(login_url='login-page')
def teamworkfilepage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        designation = request.POST.get('designation')
        department=request.POST.get('department')
        files = request.FILES['files']
        file = filesend()
        file.Name = name
        file.Designation = designation
        file.Files = files
        file.Department = department
        file.save()
    return render(request, 'tlworkfilepage.html')


@login_required(login_url='login-page')
def files(request):
    form = fileform()
    if request.method == 'POST':
        form = filesend(request.POST)
        if form.is_valid():
            form.save()
        return redirect('employer')
    context = {'form': form}
    return render(request, 'editfile.html', context)


@login_required(login_url='login-page')
def edit(request, pk):
    updatefile = filesend.objects.get(id=pk)
    form = fileform(instance=updatefile)

    if request.method == 'POST':
        form = fileform(request.POST, instance=updatefile)
        if form.is_valid():
            form.save()
        return redirect('employer')

    context = {'form': form}
    return render(request, 'editfile.html', context)


@login_required(login_url='login-page')
def edit1(request, pk):
    updatefile = filesend.objects.get(id=pk)
    form = fileform(instance=updatefile)

    if request.method == 'POST':
        form = fileform(request.POST, instance=updatefile)
        if form.is_valid():
            form.save()
        return redirect('manager')

    context = {'form': form}
    return render(request, 'editfile.html', context)

def update1(request,pk):
    if request.method=='POST':
        files = request.FILES['files']

        file = filesend()
        file.save()


        filesend.objects.filter(id=pk).update(Files=files)
        return redirect('manager')
    else:
        return render(request,'update.html')

def update(request,pk):
    if request.method=='POST':
        files = request.FILES['files']

        file = filesend()
        file.save()


        filesend.objects.filter(id=pk).update(Files=files)
        return redirect('manager')
    else:
        return render(request,'update.html')




def registerpage(request):
    form = registerform()
    if request.method == 'POST':
        form = registerform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login-page')
    context = {'form': form}
    return render(request, 'register.html', context)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user.is_teamleader:
            login(request, user)
            return redirect('tlhome')
        if user.is_manager:
            login(request, user)
            return redirect('manager')
        if  user.is_employer:
            login(request, user)
            return redirect('employer')

    return render(request, 'main.html')


def logoutuser(request):
    logout(request)
    return redirect('login-page')



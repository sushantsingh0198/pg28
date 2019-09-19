from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import *
import io
import csv


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username already taken')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            email=email, password=password)
            user.save()
            return render(request, 'verification.html')
    else:
        return render(request, 'signup.html')


def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, 'registration/login.html')
    else:
        return render(request, 'registration/login.html')


def add_teacher(request):
    if request.method == 'POST':
        name = request.POST['name']
        e_code = request.POST['e_code']
        available_load = request.POST['load']
        if TeacherDetail.objects.filter(e_code=e_code):
            messages.info(request, 'Teacher already added')
            return redirect('add_teacher')
        else:
            teacher = TeacherDetail(name=name, e_code=e_code, available_load=available_load)
            teacher.save()
            messages.info(request, 'Added Successfully')
            return redirect('add_teacher')
    else:
        return render(request, 'add_teacher.html')


def import_teacher_detail(request):
    if request.method == 'GET':
        return render(request, 'import_teacher_detail.html')
    file = request.FILES['file']
    if not file.name.endswith('.csv'):
        messages.error(request, 'File Uploaded is not in csv file')
    data_set = file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = TeacherDetail.objects.update_or_create(
            name=column[0],
            e_code=column[1],
            available_load=column[3]
        )
    messages.info(request, 'Uploaded Successfully')
    return redirect('home')


def remove_teacher(request):
    return render(request, 'remove_teacher.html')


def add_class(request):
    if request.method == 'POST':
        sem = request.POST['sem']
        cls = request.POST['cls']
        class_detail = ClassDetail(sem=sem, cls=cls)
        class_detail.save()
        messages.info(request, 'Added Successfully')
        return redirect('add_class')
    else:
        return render(request, 'add_class.html')


def import_class_detaail(request):
    if request.method == 'POST':
        return render(request,'import_class_detail.html')
    else:
        return render(request, 'import_class_detail.html')


def remove_class(request):
    return render(request, 'remove_class.html')


def view_load_list(request):
    return render(request, 'view_load_list.html')


def viwe_individual(request):
    return render(request, 'view_individual.html')

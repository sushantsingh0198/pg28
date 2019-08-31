from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages


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
        # elif User.objects.filter(email=email).exists():
        #     messages.info(request,'Email already registered')
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


def change_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        password = request.POST['password']
        user = pa

    else:
        return render(request,'registration/login.html')

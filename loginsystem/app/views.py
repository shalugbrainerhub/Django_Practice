
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):
    return render(request, 'app/index.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        print(firstname)
        lastname=request.POST['lastname']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name=firstname
        print(myuser.first_name)
        myuser.last_name=lastname
        myuser.save()
        messages.success(request, "Your account has been created.")
        return redirect('signin')

    return render(request, 'app/signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        print(username, password1)
        user=authenticate(request,username=username, password=password1)
        print(user)
        if user is not None:
            login(request, user)
            return render(request, "app/index.html", {'user': request.user})
        else:
            print("Wrong credentials!!")
            messages.error(request, "Wrong credentials!!")
            return redirect('home')
    return render(request,'app/signin.html')

def signout(request):
    logout(request)
    return redirect('home')
    
  


from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def homepage(request):
    return render(request,'website.html')

def logoutpage(request):
    logout(request)
    return redirect('login')

def loginpage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'user name or password incorrect')
    return render(request,'login.html')

def registerpage(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        uname=request.POST['username']
        messages.success(request,'Account created Successfully for '+uname)
        return redirect('login') 
    return render(request,'register.html',{'form':form})


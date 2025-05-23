from django.shortcuts import render,redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def user_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        else:
             messages.error(request, 'Please check and try again.')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html',{"form":form})
        

def user_login(request):
        form = UserLoginForm(request.POST)
        if request.method == "POST":
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username,password=password)
                
                if user is not None:
                    login(request,user)
                    return redirect('home')
                else:
                    messages.error(request, 'Invalid username or password')
            else:
                form= UserLoginForm()
            
        return render(request,'login.html',{"form":form})
    
    
def home(request):
    
    return render(request, 'home.html')


def user_logout(request):
    logout(request)
    return render(request, 'login.html')
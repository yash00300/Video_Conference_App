from django.shortcuts import render,redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
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
        

@login_required
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
    

@login_required
def home(request):
    first_name = request.user.first_name
    return render(request, 'home.html',{"first_name":first_name})


@login_required
def video_conf(request):
    name = request.user.first_name 
    last_name = request.user.last_name
    return render(request, 'video_conf.html', {'name': name, 'last': last_name})


@login_required
def join_room(request):
    if request.method == "POST":
        roomID = request.POST.get('roomID')
        if roomID:  # Make sure it's not None or empty
            return redirect("/meeting?roomID=" + roomID)
        else:
            return render(request, 'joinroom.html', {"error": "Room ID is required."})
    return render(request, 'joinroom.html')


def user_logout(request):
    logout(request)    
    return render(request, 'login.html')
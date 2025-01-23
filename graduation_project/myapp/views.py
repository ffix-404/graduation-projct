from django.shortcuts import render, redirect,HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages

def signin_login(request):
    if request.method == 'POST':
        if 'signup' in request.POST:  # Sign Up Form
            username = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            # Check if user already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists')
                return redirect('signin_login')
            
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return HttpResponseRedirect('signin_login')
                
            # Create new user
            try:
                user = User.objects.create_user(username=username, 
                                              email=email, 
                                              password=password)
                login(request, user)
                return redirect('home')  # Redirect to home page
            except Exception as e:
                messages.error(request, f'Error creating user: {str(e)}')
                return redirect('signin_login')
            
        elif 'signin' in request.POST:  # Sign In Form
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            # Get username from email
            try:
                user = User.objects.get(email=email)
                username = user.username
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')  # Redirect to home page
                else:
                    messages.error(request, 'Invalid credentials')
            except User.DoesNotExist:
                messages.error(request, 'User does not exist')
            
    return render(request, 'sigin_log_in.html')

def home(request):
    return render(request, 'home.html')
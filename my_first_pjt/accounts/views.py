from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignupForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:index')
            else:
                messages.error(request, '로그인에 실패했습니다. 다시 시도해주세요.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            new_user = User.objects.create_user(username=username, email=email, password=password)
            login(request, new_user)
            return redirect('main:index')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def profile_view(request):
    # ... 프로필 관리 기능 구현 ...
    return render(request, 'accounts/profile.html')

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.views.generic.edit import FormView
from django.contrib import messages
from .forms import SignUpForm, SignInForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        print(request.user.username)
        user = User.objects.get(username=request.user.username)
        # role = user.user_role.lower()
        return redirect('users:dashboard')
    else:
        return redirect(reverse('login'))


def signIn(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=username,
                                password=raw_password)
            if user is not None:
                login(request, user)
                messages.success(request, 'successfully login')
                return redirect('home')
            else:
                messages.error(
                    request, 'Please enter correct username and password combination')
                return redirect('/')
    else:
        form = SignInForm()
    return render(request, 'accounts/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Please enter correct username and password combination')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html', {'form': form})
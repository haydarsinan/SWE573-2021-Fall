from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from Members.forms import signUpForm, editProfilePage
from ServicEventPool.models import Profile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, "Your password or username or both are not correct!")
            return redirect('login')
    else:
        return render(request, 'authentication/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out!")
    return redirect('home')


def register_user(request):
    if request.method == "POST":
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            newProfile = Profile.objects.create(user=user)
            newProfile.save()
            login(request, user)
            messages.success(request, "You successfully registered!")
            return redirect('home')
    else:
        form = signUpForm()
    return render(request, 'authentication/register_user.html', {
        'form': form,
    })


def update_user(request):
    if request.method == "POST":
        form = editProfilePage(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "You successfully updated!")
            return redirect('home')
    else:
        form = editProfilePage(instance=request.user)
    return render(request, 'authentication/update_profile.html', {
        'form': form,
    })

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'The password is not updated!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'authentication/change_password.html', {
        'form': form
    })
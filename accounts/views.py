from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile
from django.contrib.auth.decorators import login_required
from skills.models import Skill
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')

# REGISTER
def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error':'User exists'})

        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user)

        return redirect('login')

    return render(request, 'register.html')

# LOGIN
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')

# LOGOUT
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    profile = request.user.profile
    skills = Skill.objects.all()

    if request.method == 'POST':
        teach_ids = request.POST.getlist('teach')
        learn_ids = request.POST.getlist('learn')

        profile.skills_teach.set(teach_ids)
        profile.skills_learn.set(learn_ids)

        return redirect('profile')

    return render(request, 'profile.html', {
        'profile': profile,
        'skills': skills
    })

@login_required
def browse_users(request):
    skill_query = request.GET.get('skill')

    users = Profile.objects.exclude(user=request.user)

    if skill_query:
        users = users.filter(
            skills_teach__name__icontains=skill_query
        )

    return render(request, 'browse.html', {
        'users': users,
        'skill_query': skill_query
    })

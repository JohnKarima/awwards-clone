from django.shortcuts import render, redirect
from django.contrib import messages
from django.http  import HttpResponse
from .models import Profile, Project, User
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProjectUploadForm
from django.contrib.auth.decorators import login_required
from cloudinary.forms import cl_init_js_callbacks
from django.core.exceptions import ObjectDoesNotExist

@login_required
def index(request):
    projects = Project.objects.all()
    users = User.objects.all()
    return render(request, 'index.html', {"projects":projects[::-1], "users": users})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Successfully created account created for {username}! Please log in to continue')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def update(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,
        instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Successfully updated your account!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/update.html', context)

@login_required
def upload_project(request):
    if request.method == "POST":
        form = ProjectUploadForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit = False)
            project.user = request.user.profile
            project.save()
            messages.success(request, f'Successfully uploaded your Project!')
            return redirect('index')
    else:
        form = ProjectUploadForm()
    return render(request, 'upload_project.html', {"form": form})
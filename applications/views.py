from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import  login_required
from django.contrib.auth.models import  User
from django.contrib.auth import  authenticate, login, logout
from .models import Application


def get_login(request):
    return render(request, "applications/auth/login.html")


def post_login(request):
    user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
    if user is not None:
        login(request, user)
    else:
        raise Exception("User is None")
    return redirect(reverse("applications:index"))


def logoutUser(request):
    logout(request)
    return redirect(reverse("applications:get_login"))

def get_register(request):
    return render(request, "applications/auth/register.html")


def post_register(request):
    user = User(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"])
    user.save()
    authenticate(request, username=user.username, password=request.POST["password"])
    login(request, user)
    return redirect(reverse("applications:index"))


@login_required
def index(request):
    applications = request.user.application_set.all()
    return render(request, "applications/index.html", {"apps": applications})


@login_required
def add_app(request):
    return render(request, "applications/create.html")


@login_required
def save_app(request):
    application = Application(name=request.POST["name"],
                              website=request.POST["website"],
                              additional_info=request.POST["additional_info"],
                              user=request.user)
    application.save()
    return redirect(reverse("applications:index"))


@login_required
def show_app(request, app_id):
    app = Application.objects.get(pk=app_id)
    return render(request, "applications/show.html", {"app": app})


@login_required
def edit_app(request, app_id):
    app = Application.objects.get(pk=app_id)
    return render(request, "applications/edit.html", {"app": app})


@login_required
def update_app(request, app_id):
    app = Application.objects.get(pk=app_id)
    app.name = request.POST["name"]
    app.website = request.POST["website"]
    app.additional_info = request.POST["additional_info"]
    app.save()
    return redirect(reverse("applications:index"))


@login_required
def delete_app(request, app_id):
    app = Application.objects.get(pk=app_id)
    app.delete()
    return redirect(reverse("applications:index"))


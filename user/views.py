from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def login_user(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        data = authenticate(username=username, password=password)
        if data is not None:
            login(request,data)
            return redirect("admin/")

    context = {"form": form}
    return render(request, "user/login.html", context)

def home(request):
    return render(request,'user/home.html')
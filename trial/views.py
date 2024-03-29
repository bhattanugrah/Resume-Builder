#from django.shortcuts import render, redirect
#from django.contrib.auth import authenticate, login
from .forms import UsersRegisterForm, personal_information
from django.contrib.auth import logout
from django.http import HttpResponseRedirect

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UsersLoginForm

def login_view(request):
    form = UsersLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect("/")
    return render(request, "trial/form.html", {
        "form" : form,
        "title" : "Login",
    })

def register_view(request):
        form = UsersRegisterForm(request.POST or None)
        if form.is_valid():
                user = form.save()
                password = form.cleaned_data.get("password")
                user.set_password(password)
                user.save()
                new_user = authenticate(username = user.username, password = password)
                login(request, new_user)
                return redirect("/accounts/login")
        return render(request, "trial/form.html", {
                "title" : "Register",
                "form" : form,
        })

def personal_information_view(request):
    form = personal_information(request.POST or None)
    if request.method == "POST":
        form = personal_information(request.POST)["Personal_Information"]
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/index/')
        else:
            print(form.errors)
    return render(request, "trial/personal_information.html", {
        "title" : "Personal Information",
        "form" : form,
    })



def logout_view(request):
         logout(request)
         return HttpResponseRedirect("/")



def index_view(request):
        return render(request, 'index.html')

def resume_form(request):
    return render(request, 'Resume_builder_1.html')




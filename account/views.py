from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserEditForm


# Create your views here.


def user_login(request):
    if request.user.is_authenticated == True:
        return redirect('home_app:main')


    if request.method == "POST":
        # username = request.POST["username"]
        # password = request.POST["password"]
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect('home_app:main')
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home_app:main')
        
    else:
        form = LoginForm()    

    return render(request, "account/login.html", {"form": form})



def user_register(request):
    context = {"errors": []}

    if request.user.is_authenticated == True:
        return redirect('home_app:main')
    
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            context["errors"].append("The passwords are not the same")
            return render(request, "account/register.html", context)
        
        # if User.objects.get(username=username):
        #     context["errors"].append("The username already exists")
        #     return render(request, "account/register.html", context)

        user = User.objects.create(username=username, password=password1, email=email)
        login(request, user)
        return redirect('home_app:main')

    return render(request, "account/register.html", {})



def user_edit(request):
    user = request.user
    form = UserEditForm(instance=user)
    if request.method == "POST":
        form = UserEditForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()

    return render(request, "account/edit.html", {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home_app:main')
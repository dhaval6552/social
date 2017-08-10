from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Profile_final
from django.shortcuts import render,redirect
from django.contrib.auth import (
authenticate,
get_user_model,
login,
logout
)
from .forms import UserLoginForm,UserRegisterForm,UserProfileForm
def login_view(request):
    title="login"
    form=UserLoginForm(request.POST)
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        login(request,user)
        return redirect("home")
    return render(request,"login.html",{'form':form ,"title":title})


def register_view(request):
    title="register"
    form=UserRegisterForm(request.POST)
    if form.is_valid():
        user=form.save(commit=False)
        password=form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user=authenticate(username=user.username,password=password)
        login(request,new_user)
        return redirect("login.html")
    return render(request,"register.html",{'form':form,'title':title})


def logout_view(request):
    return render(request,"logout.html",{})

# def home(request):
def home(request):
    user_all=User.objects.all()
    return render(request,"home.html",{'user_all':user_all})

def profile(request,id=id):
    #user_id = int(request.POST['id'])
    object = User.objects.get(id=id)
    # image=Profile_final.objects.get('profile_image')

    return render(request,'profile.html',{'object':object})

def edit_profile(request):
    title='upload'
    form = UserProfileForm(request.POST,request.FILES)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.user=request.user
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    return render(request,'edit_profile.html',{'title':title,'form':form})
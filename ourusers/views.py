from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from.models import UserProfile
from django.contrib import messages
from . forms import userregistrationform,UserProfileForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    # print(request.method)
    if request.method == 'POST':
        form = userregistrationform(request.POST)
        profile_form=UserProfileForm(request.POST,request.FILES)

        # print(form.is_valid)
        # print(profile_form.is_valid)
        if form.is_valid() and profile_form.is_valid():
            user= form.save()
            profile=profile_form.save(commit=False)
            profile.user=user

            profile.save()


            username= form.cleaned_data.get('username')
            messages.success(request,f'Account created successfully for {username}')
            return redirect('/login')

        else:

            messages.error(request,f"Error: {form.errors}")
            # return render(request,'register.html',{'form':form})
            return redirect('/register')

    else:
        form = userregistrationform()
        profile_form = UserProfileForm(request.POST)
        return render(request,'register.html',{'form':form,'pform':profile_form})
def loginpage(request):
    if request.method=='POST':

        username=request.POST['username']
        password=request.POST['password']
        promo=request.POST['promo']
        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            seconndtable_details=UserProfile.objects.get(user=user)
            # context={'email':user.email,'fname':seconndtable_details.fname,'lname':seconndtable_details.lname,'address':seconndtable_details.address}
            if promo=="doctor":

                return render(request,'docdashboard.html',{'email':user.email,'fname':seconndtable_details.fname,'lname':seconndtable_details.lname,'address':seconndtable_details.address})
            else:
                return render(request,'home.html',{'email':user.email,'fname':seconndtable_details.fname,'lname':seconndtable_details.lname,'address':seconndtable_details.address})
        else:
            messages.error(request,f'password or username is incorrect')
    return render(request,'login.html')


@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def logoutpage(request):
    logout(request)
    return redirect('login')
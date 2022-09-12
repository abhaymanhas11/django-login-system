from django.shortcuts import render,HttpResponseRedirect
from.forms import signupform
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout


def register(request):
    if request.method == 'POST':
        f = signupform(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
    else:
        f = signupform()
    return render(request, 'register.html', {'form': f})


# login user
def Login(request):
    if not request.user.is_authenticated:
       if request.method=='POST':
         fm=AuthenticationForm(request=request,data=request.POST)
         if fm.is_valid():
             uname=fm.cleaned_data['username']
             pname=fm.cleaned_data['password']
             user=authenticate(username=uname,password=pname)
             if user is not None:
                 login(request,user)
                 return HttpResponseRedirect('/profile/')
       else:
           fm=AuthenticationForm()
       return render(request,'login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

# user login profile
def user_profile(request):
    if request.user.is_authenticated:
       return render(request,'proflile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
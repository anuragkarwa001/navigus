from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.template import RequestContext
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def login_page(request):
    return render(request,"authentication/login.html")

def signup_page(request):
    return render(request,"authentication/registration.html")

def view_page(request):
    if  request.user.is_authenticated==True:
        return HttpResponse("<a href='/authentication/logout' >logout </a>       view the page")
    else :
        
        return redirect("/authentication/login_page")
def logout(request):

     auth.logout(request)
     return redirect("/authentication/login_page")



def login(request):

    username=request.POST['username']
    password=request.POST['password']
    
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return redirect('/authentication/login_page/view_page')
    else:
        return messages.info(request,"invalid credentials")
        #return HttpResponse("failure")
        





    

def signup(request):

     
     first_name=request.POST['name']
     password=request.POST['password']
     email=request.POST['iEmail']
  
     user=User.objects.create_user(username=email,password=password,email=email,first_name=first_name)
     user.save()
     return HttpResponse("user created")



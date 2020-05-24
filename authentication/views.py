from django.shortcuts import render,redirect
from django.http import HttpResponse 
from django.template import RequestContext
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.utils import timezone
from django.contrib.sessions.models import Session
from django.db import IntegrityError

# Create your views here.
def get_current_users():
    active_sessions = Session.objects.filter(expire_date__gte=timezone.now())
    user_id_list = []
    for session in active_sessions:
        data = session.get_decoded()
        user_id_list.append(data.get('_auth_user_id', None))
    # Query all logged in users based on id list
    return User.objects.filter(id__in=user_id_list)

def home_page(request):
    return render(request,"authentication/secret_file.html",)


def login_page(request):
    return render(request,"authentication/login.html")

def signup_page(request):
    return render(request,"authentication/registration.html")

def view_page(request):
    if  request.user.is_authenticated==True:

        
        
        print(get_current_users())
        return render(request,"authentication/secret_file.html",{'users':get_current_users()})
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
        messages.info(request,"invalid credentials")
        return render(request,'authentication/login.html')
        

def signup(request):

     
     first_name=request.POST['name']
     password=request.POST['password']
     email=request.POST['iEmail']
     try: 
        user=User.objects.create_user(username=email,password=password,email=email,first_name=first_name)
        user.save()
     except IntegrityError as e:
         messages.info(request,"user already exists")
         return render(request,"authentication/registration.html")

     messages.info(request,"Thank you for creating an account")
     return render(request,"authentication/secret_file.html")



from django.urls import path
from . import views

urlpatterns=[
    path('login_page/',views.login_page,name='login_page'),
    path('signup_page/',views.signup_page,name='signup_page'),
    path('login_page/login',views.login,name='login'),
    path('signup_page/signup',views.signup,name='signup')
]
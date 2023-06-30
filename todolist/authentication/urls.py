from .views import *

from django.urls import path

urlpatterns = [
    path("login/",login_page,name="login"),
    path("logout/",logout_user,name="logout"),
    path("signup/",signup,name="signup"),


    



]

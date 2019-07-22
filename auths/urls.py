from . import views
from django.urls import path
app_name="auths"

urlpatterns = [

    path("register/",views.register,name="register"),
    path("login/",views.loginUser,name="login"),
    path("logout/",views.logoutUser,name="logout"),

    
]
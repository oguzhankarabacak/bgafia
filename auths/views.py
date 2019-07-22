from django.shortcuts import render,redirect
from .forms import RegisterForm
from requests import get,request
from django.contrib.auth.models import User
from .models import UserData
from django.contrib.auth import login,authenticate



# Create your views here.


def get_ip_address():
    ip = get('https://api.ipify.org').text
    print(ip)
#print('My public IP address is: {}'.format(ip))
    data=get("http://ip-api.com/json/"+str(ip)).json()
    print(data.get("city"))
    print(data.get("country"))
    datas={"ip":ip,"city":data.get("city"),"country":data.get("country")}
    return datas

def register(request):
    form=RegisterForm(request.POST or None)
    # print("*******************************************************************")
    # print(form)
    # print("*******************************************************************")

    if form.is_valid():

        print("------------------------------------------------------***************************")
        print(form.cleaned_data)
        print("------------------------------------------------------***************************")

        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        first_name=form.cleaned_data.get("first_name")
        last_name=form.cleaned_data.get("last_name")
        email=form.cleaned_data.get("email")
        birthday=form.cleaned_data.get("birthday")
        print("--------------------------------------")
        print(username,password,first_name,last_name,email,birthday)
        print("--------------------------------------")

        newUser=User(username=username,first_name=first_name,last_name=last_name,email=email)
        newUser.set_password(password)
        newUser.save()
        print("-------------------------------------------")
        datas=get_ip_address()
        # print(datas["city"])
        # print(datas["ip"])
        # print(datas["country"])
        
        
        
        print("-------------------------------------------")
        newUserData=UserData(ip_address=datas["ip"],city=datas["city"],country=datas["country"],birthday=birthday)
        newUserData.user=newUser
        newUserData.save()
        login(request,newUser)
        return redirect("index")
    context={"form":form}
    return render(request,"register.html",context)
        
    context={"form":form}
    return render(request,"register.html",context)

def logoutUser(request):
    pass

def loginUser(request):
    return render(request,"login.html")

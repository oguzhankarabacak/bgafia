from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from requests import get,request
from django.contrib.auth.models import User
from .models import UserData
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages



# Create your views here.

#<--- ip işlemleri --> 

def get_ip_address():
    ip = get('https://api.ipify.org').text
    print(ip)
#print('My public IP address is: {}'.format(ip))
    data=get("http://ip-api.com/json/"+str(ip)).json()
    print(data.get("city"))
    print(data.get("country"))
    datas={"ip":ip,"city":data.get("city"),"country":data.get("country")}
    return datas

#<--- register işlemleri --> 

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
        messages.success(request,"Kayıt Başarıyla Tamamlandı")
        return redirect("index")
    context={"form":form}
    return render(request,"register.html",context)
        
    context={"form":form}
    return render(request,"register.html",context)


#<--- login işlemleri --> 

def loginUser(request):
    form=LoginForm(request.POST or None)
    print("*******************************************")
    print(form)
    print("****************************************")

    context={"form":form}

    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        print("*******************************************")
        print(username,password)
        print("****************************************")

        user=authenticate(username=username,password=password)
        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)

        messages.success(request,"başarı ile giriş yaptınız")
        login(request,user)

        return redirect("index")

    return render(request,"login.html",context)    

#<--- logout işlemleri --> 
def logoutUser(request):
    logout(request)
    messages.warning(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")


#<---Profile Yönlendir --->
def profile(request):
    current_user=request.user  #user=username
    default_user=User.objects.get(username=current_user)
    
    profile_info={"username":default_user.username,"first_name":default_user.first_name
    ,"last_name":default_user.last_name,"email":default_user.email,"birthday":default_user.userdata.birthday}   
    return render(request,"profile.html",profile_info)
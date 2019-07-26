from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    first_name=forms.CharField(max_length=30,label="İsim",required=True)
    last_name=forms.CharField(max_length=30,label="Soyisim",required=True)
    username=forms.CharField(max_length=50,label="Kullanıcı Adı",required=True)
    password=forms.CharField(max_length=20,min_length=8,label="Parola",widget=forms.PasswordInput,required=True)
    confirm=forms.CharField(max_length=20,min_length=8,label="Parola Doğrula",widget=forms.PasswordInput,required=True)
    email=forms.EmailField(required=True,label="email")
    birthday=forms.DateField(label="Doğum tarihi",required=True)

    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")
        first_name=self.cleaned_data.get("first_name")
        last_name=self.cleaned_data.get("last_name")
        email=self.cleaned_data.get("email").lower()
        birthday=self.cleaned_data.get("birthday")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Kullanıcı Adı sistemde Kayıtlı")
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Sistemde Kayıtlı")

        if (password and confirm and password != confirm):
            raise forms.ValidationError("Parolalar Eşleşmiyor")

        if password == "12345678":
            raise forms.ValidationError("Lütfen Güçlü Bir parola Giriniz")
        
        

        values={"username":username,"password":password,"birthday":birthday
        ,"first_name":first_name,"last_name":last_name,"email":email}

        return values


class LoginForm(forms.Form):
    username=forms.CharField(required=True,label="username")
    password=forms.CharField(label="parola",widget=forms.PasswordInput)
    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        values={"username":username,"password":password}

        return values
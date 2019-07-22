from django import forms

class RegisterForm(forms.Form):
    first_name=forms.CharField(max_length=30,label="İsim")
    last_name=forms.CharField(max_length=30,label="Soyisim")
    username=forms.CharField(max_length=50,label="Kullanıcı Adı")
    password=forms.CharField(max_length=20,min_length=8,label="Parola",widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=20,min_length=8,label="Parola Doğrula",widget=forms.PasswordInput)
    email=forms.EmailField()
    birthday=forms.DateField(label="Doğum tarihi")

    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        confirm=self.cleaned_data.get("confirm")
        first_name=self.cleaned_data.get("first_name")
        last_name=self.cleaned_data.get("last_name")
        email=self.cleaned_data.get("email")
        birthday=self.cleaned_data.get("birthday")

        if (password and confirm and password != confirm):
            raise forms.ValidationError("Parolalar Eşleşmiyor")

        values={"username":username,"password":password,"birthday":birthday
        ,"first_name":first_name,"last_name":last_name,"email":email}

        return values
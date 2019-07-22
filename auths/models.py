from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserData(models.Model):
    cities=(
        ('Konya','Konya'),
        ('Istanbul','Istanbul')
    )
    ip_address=models.CharField(max_length=50,null=False,verbose_name="ip")
    city=models.CharField(max_length=30,null=False,verbose_name="city",choices=cities)
    country=models.CharField(max_length=30,null=False,verbose_name="country")
    birthday=models.DateField(blank=False,null=True,verbose_name="Doğum Tarihi")
    user=models.OneToOneField(User,null=False,verbose_name="User",on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Kullanıcı Verileri'

    def __str__(self):
        return "%s UserData" % self.user.username


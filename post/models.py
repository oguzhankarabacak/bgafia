from django.db import models

# Create your models here.
class UserPost(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar",blank=False)
    title=models.CharField(max_length=50,blank=False,verbose_name="Başlık")
    content=models.TextField(max_length=250,blank=False,verbose_name="Gönderi")
    cities=(
        ('Konya','Konya'),
        ('Istanbul','Istanbul')
    )
    to_city=models.CharField(max_length=20,choices=cities,verbose_name="Şehir")
    created_date=models.DateTimeField(auto_now_add=True)
    # from_city=models.CharField(max_length=20)


    def __str__(self):
        return self.title
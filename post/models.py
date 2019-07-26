from django.db import models

# Create your models here.
class UserPost(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar",blank=False)
    title=models.CharField(max_length=50,blank=False,verbose_name="Başlık")
    content=models.TextField(max_length=500,blank=False,verbose_name="Gönderi")
    cities=(
        ('Adana','Adana'),('Adıyaman','Adıyaman'),('Afyon','Afyon'),
('Agri','Agri'),('Amasya','Amasya'),('Ankara','Ankara'),('Antalya','Antalya'),('Artvin','Artvin'),
('Aydin','Aydin'),('Balikesir','Balikesir'),('Bilecik','Bilecik'),('Bingöl','Bingöl'),('Bitlis','Bitlis'),
('Bolu','Bolu'),('Burdur','Burdur'),('Bursa','Bursa'),('Canakkale','Canakkale'),('Cankiri','Cankiri'),('Corum','Corum'),
('Denizli','Denizli'),('Diyarbakir','Diyarbakir'),('Edirne','Edirne'),('Elazig','Elazig'),('Erzincan','Erzincan'),
('Erzurum','Erzurum'),('Eskisehir','Eskisehir'),('Gaziantep','Gaziantep'),('Giresun','Giresun'),('Gumushane','Gumushane'),('Hakkari','Hakkari'),
('Hatay','Hatay'),('Isparta','Isparta'),('Mersin','Mersin'),('Istanbul','Istanbul'),('Izmir','Izmir'),('Kars','Kars'),('Kastamonu','Kastamonu'),
('Kayseri','Kayseri'),('Kirklareli','Kirklareli'),('Kirşehir','Kirşehir'),('Kocaeli','Kocaeli'),('Konya','Konya'),('Kutahya','Kutahya'),('Malatya','Malatya'),
('Manisa','Manisa'),('Kahramanmaras','Kahramanmaras'),('Mardin','Mardin'),('Mugla','Mugla'),('Mus','Mus'),('Nevsehir','Nevsehir'),
('Nigde','Nigde'),('Ordu','Ordu'),('Rize','Rize'),('Sakarya','Sakarya'),('Samsun','Samsun'),
('Siirt','Siirt'),('Sinop','Sinop'),('Sivas','Sivas'),('Tekirdag','Tekirdag'),
('Tokat','Tokat'),('Trabzon','Trabzon'),('Tunceli','Tunceli'),('Sanliurfa','Sanliurfa'),('Usak','Usak'),
('Van','Van'),('Yozgat','Yozgat'),('Zonguldak','Zonguldak'),('Aksaray','Aksaray'),('Bayburt','Bayburt'),
('Karaman','Karaman'),('Kirikkale','Kirikkale'),('Batman','Batman'),('Sirnak','Sirnak'),('Bartin','Bartin'),
('Ardahan','Ardahan'),('Iğdir','Iğdir'),('Yalova','Yalova'),('Karabuk','Karabuk'),('Kilis','Kilis'),
('Osmaniye','Osmaniye'),('Düzce','Düzce'))
    to_city=models.CharField(max_length=20,choices=cities,verbose_name="Şehir")
    created_date=models.DateTimeField(auto_now_add=True)
    comment_number=models.IntegerField(default=0)
    # from_city=models.CharField(max_length=20)


    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_date']

class Comment(models.Model):
    post=models.ForeignKey(UserPost,on_delete=models.CASCADE,verbose_name="UserPost",related_name="comments")
    comment_author=models.CharField(max_length=50,verbose_name="isim")
    comment_content=models.CharField(max_length=200,verbose_name="Yorum")
    comment_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']
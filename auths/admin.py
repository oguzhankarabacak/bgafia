from django.contrib import admin
from .models import UserData



@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display=["user","ip_address","city","country","birthday",]
    list_display_links=["user"]
    search_fields=["user","country","city"]
    

    class Meta:
        model=UserData

# Register your models here.

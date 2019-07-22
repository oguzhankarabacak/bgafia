from django.contrib import admin
from .models import UserPost

admin.site.register(UserPost)

class User_PostAdmin(admin.ModelAdmin):
    list_display=["id","title","author","created_date"]
    list_display_links=["id","title"]
    search_fields=["title","author","id"]
    list_filter=["created_date"]

    class Meta:
        model=UserPost
# Register your models here.

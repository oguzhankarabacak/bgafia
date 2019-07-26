from django.contrib import admin
from .models import UserPost,Comment


@admin.register(UserPost)
class User_PostAdmin(admin.ModelAdmin):
    list_display=["id","title","author","created_date","to_city"]
    list_display_links=["id","title"]
    search_fields=["title","author","id"]
    list_filter=["created_date"]

    class Meta:
        model=UserPost

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=["id","comment_author","post_id","comment_date"]
    list_display_links=["id"]
    search_fields=["title","comment_author","post_id"]
    list_filter=["comment_date"]

# Register your models here.

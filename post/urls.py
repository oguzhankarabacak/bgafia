from . import views
from django.urls import path
app_name="post"

urlpatterns = [
    path("mypost",views.mypost,name="mypost"),
    path("create",views.addPost,name="create"),
    path("delete/<int:id>",views.postDelete,name="delete"),
    path("update/<int:id>",views.postUpdate,name="update"),
    path("detail/<int:id>",views.detail,name="detail"),
    path("posts",views.posts,name="posts"),
    path("comment/<int:id>",views.addComment,name="comment")

    
    
]
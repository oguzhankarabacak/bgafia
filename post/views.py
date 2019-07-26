from django.shortcuts import render,redirect,get_object_or_404,reverse
from .forms import PostForm
from django.contrib import messages
from .models import UserPost,Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
#<---Anasayfaya Yönlendir --->
def index(request):
    form=PostForm(request.POST or None)
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"Gönderiniz Oluşturuldu")
        return redirect("index")

    content={"form":form}
    return render(request,"index.html",content)


#<---Hakkımızda Yönlendir --->
def about(request):
    return render(request,"about.html")


#<---Postlarıma Yönlendir --->
@login_required(login_url="auths:login")
def mypost(request):
    posts=UserPost.objects.filter(author=request.user)
    content={"posts":posts}
    return render(request,"mypost.html",content)

#<---Post Ekle --->
@login_required(login_url="auths:login")
def addPost(request):
    form=PostForm(request.POST or None)
    if form.is_valid():

        form=form.save(commit=False)
        form.comment_number=0
        form.author=request.user
        form.save()
        messages.success(request,"Gönderiniz Oluşturuldu")
        return redirect("index")

    content={"form":form}
    return render(request,"addpost.html",content)

# Makaleyi Silme
@login_required(login_url="auths:login")
def postDelete(request,id):
    post=UserPost.objects.filter(id=id,author=request.user).first()
    if (post is None):
        return render(request,"index.html")

    post.delete()
    messages.success(request,"Başarıyla Silindi")
    return redirect("post:mypost")   

# Post Güncelleme
@login_required(login_url="auths:login")
def postUpdate(request,id):
    post=UserPost.objects.filter(id=id).first()
    form=PostForm(request.POST or None,instance=post)
    if form.is_valid():
        post=form.save(commit=False)
        post.author=request.user
        post.save()
        messages.success(request,"Gönderiniz Güncellendi")
        return redirect("index")
    content={"form":form}
    return render(request,"update.html",content)




#Post Detay Sayfası
@login_required(login_url="auths:login")
def detail(request,id):
    post=UserPost.objects.filter(id=id).first()
    print("*******************---------------------")
    print(request.user.userdata.city)
    print(post.to_city)
    print("*******************---------------------")
    if post.to_city == request.user.userdata.city or post.author_id == request.user.id:
        comments=post.comments.all()
    
        content = {
            "post":post,
            "comments":comments
        }

        return render(request,"detail.html",content)
    
    messages.info(request,"Sadece Şehrinize Ait sorulara Bakabilirsiniz")
    return redirect("index")
    
    


#Tüm Postlar
@login_required(login_url="auths:login")
def posts(request):
    
    posts=UserPost.objects.filter(to_city=request.user.userdata.city)
    return render(request,"posts.html",{"posts":posts})


# Yorum Ekle
@login_required(login_url="auths:login")
def addComment(request,id):
    post=UserPost.objects.filter(to_city=request.user.userdata.city).filter(id=id).first()


    if request.method=="POST":
        comment_content=request.POST.get("comment_content")
        comment_author=request.user
        
        newComment=Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.post=post
        newComment.save()
        post.comment_number += 1
        post.save()
    
    return redirect(reverse("post:detail",kwargs={"id":id}))
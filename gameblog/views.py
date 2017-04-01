
from .models import Post, Comment, Photo
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.http import HttpResponse


# view all posts
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'gameblog/index.html', {'posts': posts})

#detail view of a post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'gameblog/post_detail.html', {'post': post})

#add post
def post_new(request):
        form = PostForm()
        return render(request, 'gameblog/post_edit.html', {'form': form})

#photo???
def photo_list(request):
    photo = Photo.objects.all()
    return render(request, 'gameblog/post_detail.html', {'photo':photo})

#save post
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('gameblog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'gameblog/post_edit.html', {'form': form})

#edit post
def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('gameblog.views.post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'gameblog/post_edit.html', {'form': form})

# add comment
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'gameblog/add_comment_to_post.html', {'form': form})

#like post
def like_post(request):
    post_id = request.GET.get('post_id', None)

    likes = 0
    if post_id:
       post = Post.objects.get(id=int(post_id))
       if post is not None:
            likes = post.likes+1
            post.likes = likes
            post.save()

    return HttpResponse(likes)





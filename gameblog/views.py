from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect


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

#save post
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.likes = 0
            post.save()
            return redirect('gameblog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'gameblog/post_edit.html', {'form': form})

def post_edit(request, pk):
        post = get_object_or_404(Post, pk=pk)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.likes = 0
                post.save()
                return redirect('gameblog.views.post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'gameblog/post_edit.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import http404

def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, id):
    # try:
    #     post=Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise http404("Post does not exist")
    post = get_object_or_404(Post.published, id=id)
    return render(request, 'blog/post/detail.html', {'post': post})


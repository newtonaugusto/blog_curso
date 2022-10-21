from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def post_detail(request, post_id):
    post = Post.objects.filter(pk=post_id).first()
    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)

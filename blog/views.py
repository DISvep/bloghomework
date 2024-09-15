from django.shortcuts import render
from .models import Post, Author


# Create your views here.

def index(request):
    return render(
        request,
        'blog/main.html'
    )


def post_list(request):
    posts = Post.objects.all()
    context = {
        'post_list': posts
    }
    return render(
        request,
        "blog/post_list.html",
        context=context
    )


def post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    return render(
        request,
        "blog/post.html",
        context=context
    )


def author(request, author_id):
    author = Author.objects.get(id=author_id)
    posts = Post.objects.filter(author=author)
    context = {
        "author": author,
        "posts": posts
    }
    return render(
        request,
        "blog/author.html",
        context=context
    )


def author_list(request):
    authors = Author.objects.all()
    context = {
        'author_list': authors
    }
    return render(
        request,
        'blog/author_list.html',
        context=context
    )


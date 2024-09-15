from django.shortcuts import render
from .models import Post


# Create your views here.
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

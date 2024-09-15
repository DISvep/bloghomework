from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("post_list/", views.post_list, name='post_lists'),
    path("post/<int:post_id>", views.post, name='post'),
    path('author/<int:author_id>', views.author, name='author'),
    path("author_list/", views.author_list, name='author_list'),
]

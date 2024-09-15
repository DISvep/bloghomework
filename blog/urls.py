from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name='post_lists'),
    path("post/<int:post_id>", views.post, name='post')
]

from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    def published_recently(self):
        pass

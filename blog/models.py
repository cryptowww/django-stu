from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()


class Article(models.Model):
    title = models.CharField(max_length=60)
    content = models.CharField(max_length=2000)
    author = models.ManyToManyField(Author)
    pub_date = models.DateField()

from django.db import models
from django.utils import timezone
from sample.core.choices import ArticleStatus


class Article(models.Model):
    title = models.CharField(max_length=280)
    content = models.TextField()
    status = models.PositiveSmallIntegerField(
        default=ArticleStatus.UNPUBLISHED, choices=ArticleStatus.CHOICES)

    def __str__(self):
        return self.title


# Foreign key relation Book 0..* Chapters
class Book(models.Model):
    name = models.CharField(max_length=255)
    published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Chapter(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Many to many relation with it self
class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField()
    city = models.CharField(max_length=255)
    friends = models.ManyToManyField('self')

    def __str__(self):
        return self.name

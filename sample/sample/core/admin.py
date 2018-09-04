from django.contrib import admin
from sample.core.models import Article, Book, Chapter, Person

# Register your models here.
admin.site.register(Article)
admin.site.register(Book)
admin.site.register(Chapter)
admin.site.register(Person)

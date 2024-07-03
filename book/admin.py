from django.contrib import admin
from book.models import Book, Genre, Publication

# Register your models here.
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Publication)

from django.contrib import admin
from .models import Genre, Book

# Register your models here.
class GenreAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description')

class BookAdmin(admin.ModelAdmin):
	list_display = ('id', 'genre', 'name', 'author', 'year', 'description', 'link')

admin.site.register(Genre, GenreAdmin)
admin.site.register(Book, BookAdmin)
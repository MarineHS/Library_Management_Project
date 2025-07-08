from django.contrib import admin
from .models import Book

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'available')
    list_filter = ('book_of_the_month',)
    search_fields = ('title', 'author', 'isbn')
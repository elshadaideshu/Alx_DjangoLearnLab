from django.contrib import admin
from .models import Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display
    list_filter = ('author', 'publication_year')  # Filters for the sidebar
    search_fields = ('title', 'author')  # Searchable fields
admin.site.register(Book, BookAdmin)



# Register your models here.

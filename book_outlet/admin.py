from django import forms
from django.contrib import admin


from .models import Book, Author, Address

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)} #cant have both prepopulated and readonly field
    list_filter = ("rating", "author",)
    list_display = ("title", "author")



admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)

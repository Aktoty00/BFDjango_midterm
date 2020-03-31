from django.contrib import admin

from core.models import Book, Journal


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'num_pages', 'genre')


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'type', 'publisher')

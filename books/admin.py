from django.contrib import admin

from .models import Book, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'datetime_create', 'recommend', 'is_active',)

class BookAdmin(admin.ModelAdmin):
    ordering = ('-date', )

admin.site.register( Comment, CommentAdmin)
admin.site.register(Book)

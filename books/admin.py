from django.contrib import admin

from .models import Book, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'datetime_create',)


admin.site.register(Comment, CommentAdmin)
admin.site.register(Book)

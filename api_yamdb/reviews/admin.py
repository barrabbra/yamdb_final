from django.contrib import admin

from .models import Comment
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author')
    empty_value_display = '-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'review', 'author', 'text')
    empty_value_display = '-'


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)

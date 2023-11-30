from django.contrib import admin

from .models import CommentPost
# Register your models here.

class CommentPostAdmin(admin.ModelAdmin):
    list_display=('id','comment')
    list_display_links=('id','comment')

admin.site.register(CommentPost,CommentPostAdmin)

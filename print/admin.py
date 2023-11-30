from django.contrib import admin

from .models import Category, PaintPost
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス'''
    list_display=('id', 'title')
    list_display_links=('id', 'title')

class PaintPostAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス'''
    list_display=('id', 'title')
    list_display_links=('id', 'title')

# django管理サイトにCategory、CategoryAdminを登録する
admin.site.register(Category, CategoryAdmin)

# django管理サイトにPaintPost、PaintPostAdminを登録する
admin.site.register(PaintPost, PaintPostAdmin) 

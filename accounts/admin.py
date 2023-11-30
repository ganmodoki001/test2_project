from django.contrib import admin


from .models import CustomUser
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    '''管理ページのレコード一覧に表示するカラムを設定するクラス'''
    list_display=('id', 'username')
    list_display_links=('id', 'username')

# Django管理サイトにCustomUser、CustomUserAdminを登録する
admin.site.register(CustomUser, CustomUserAdmin)


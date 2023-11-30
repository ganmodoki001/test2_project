from django.db import models

from accounts.models import CustomUser
# Create your models here.

class Category(models.Model):
    '''投稿する画像のカテゴリを管理するモデル'''
    # カテゴリ名のフィールド
    title=models.CharField(
        verbose_name='カテゴリ', # フィールドのタイトル
        max_length=15
        )
    
    def __str__(self):
        '''オブジェクトを文字列に変換して返す'''
        return self.title

class PaintPost(models.Model):
    '''投稿されたデータを管理するモデル'''
    
    # CustomUserモデル(のuser_id)とPaintPostモデルを1対多の関係で結びつける。
    user= models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー', # フィールドのタイトル
        on_delete=models.CASCADE # ユーザーを削除する場合はそのユーザの投稿データも全て削除
    )
    
    # Categoryモデル(のtitle)とPaintPostモデルを1対多の関係で結びつける。
    category=models.ForeignKey(
        Category,
        verbose_name='カテゴリ', # フィールドのタイトル
        on_delete=models.PROTECT # カテゴリに関連付いたデータがあるならカテゴリを削除できない
    )
    
    # タイトル用フィールド
    title=models.CharField(
        verbose_name='タイトル', # フィールドのタイトル
        max_length=50 # 最大文字数50
    )
    
    # コメント用フィールド
    comment=models.TextField(
        verbose_name='コメント', # フィールドのタイトル
        max_length=500 # 最大文字数500
    )
    
    # 画像を文字列で投稿するためのテキストフィールド
    image=models.TextField(
        verbose_name='イラスト', # フィールドのタイトル
    )
    
    # 投稿日時のフィールド
    posted_at=models.DateTimeField(
        verbose_name='投稿日時', # フィールドのタイトル
        auto_now_add=True # 日時を自動追加
    )
    
    def __str__(self):
        '''オブジェクトを文字列にして返す'''
        return self.title
    

from django.db import models

from accounts.models import CustomUser
from print.models import PaintPost
# Create your models here.

class CommentPost(models.Model):
    '''投稿されたコメントを管理するモデル'''
    
    user= models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー',
        on_delete=models.CASCADE # ユーザーを削除する場合はそのユーザの投稿データも全て削除
    )
    
    contact_id=models.ForeignKey(
        PaintPost,
        verbose_name='ID',
        on_delete=models.CASCADE, # イラストを削除する場合はそのコメントも全て削除
        to_field="id",
        default=0
    )
    
    # コメント用フィールド
    comment=models.TextField(
        verbose_name='コメント', # フィールドのタイトル
        max_length=80, # 最大文字数500
    )
    # 投稿日時のフィールド
    posted_at=models.DateTimeField(
        verbose_name='投稿日時', # フィールドのタイトル
        auto_now_add=True, # 日時を自動追加
    )
    
    def __str__(self):
        '''オブジェクトを文字列にして返す'''
        return self.comment

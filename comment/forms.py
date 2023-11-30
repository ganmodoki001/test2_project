from django.forms import ModelForm
from .models import CommentPost

class CommentPostForm(ModelForm):
    '''モデルフォームのサブクラス'''
    class Meta:
        model=CommentPost
        fields=['comment']
    

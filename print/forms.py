from django.forms import ModelForm
from django import forms
from .models import PaintPost

class PaintPostForm(ModelForm):
    '''ModelFormのサブクラス'''
    class Meta:
        '''ModelFormのインナークラス'''
        model=PaintPost
        fields=['category','title','comment','image']


class ContactForm(forms.Form):
    # フォームのフィールドをクラス変数として定義
    name=forms.CharField(label='　　　　お名前')
    email=forms.EmailField(label='メールアドレス')
    title=forms.CharField(label='　　　　　件名')
    message=forms.CharField(label='　　メッセージ', widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        '''ContactFormのコンストラクタ
        フィールドの初期化を行う
        '''
        super().__init__(*args, **kwargs)
        # nameフィールド
        self.fields['name'].widget.attrs['placeholder']=\
            'お名前を入力してください'
        self.fields['name'].widget.attrs['class']='form-control'
        
        # emailフィールド
        self.fields['email'].widget.attrs['placeholder']=\
            'メールアドレスを入力してください'
        self.fields['email'].widget.attrs['class']='form-control'            
            
        # titleフィールド
        self.fields['title'].widget.attrs['placeholder']=\
            'タイトルを入力してください'
        self.fields['title'].widget.attrs['class']='form-control'             
            
        # messageフィールド
        self.fields['message'].widget.attrs['placeholder']=\
            'メッセージを入力してください'
        self.fields['message'].widget.attrs['class']='form-control'
from django.shortcuts import render

from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

# Create your views here.

class SignUpView(CreateView):
    '''サインアップページのビュー'''
    form_class=CustomUserCreationForm
    template_name="signup.html"
    # サインアップ完了後のリダイレクト先のURLパターン
    success_url=reverse_lazy('accounts:signup_success')
    
    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーライド
        フォームのバリデーションを通過したときに呼ばれるフォームデータの登録を行う
        '''
        # formオブジェクトのフィールドの値をデータベースに保存
        user=form.save()
        self.object=user
        return super().form_valid(form)

class SignUpSuccessView(TemplateView):
    '''サインアップ完了ページのビュー'''
    template_name="signup_success.html"
    
    
    
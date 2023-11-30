from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from django.views.generic import TemplateView, ListView, FormView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.contrib import messages
from django.core.mail import EmailMessage
from django.views.generic import DeleteView

from .forms import PaintPostForm
from .models import PaintPost
from .forms import ContactForm
# Create your views here.



class IndexView(ListView):
    '''トップページのビュー'''
    template_name='index.html'
    # order_by()を適用して投稿日時の降順で並び替える
    queryset=PaintPost.objects.order_by('-posted_at')
    # 1ページの表示件数
    paginate_by=12
    
    
# デコレーターにより、CreatePhotoViewへのアクセスはログインユーザーに限定される
# ログイン状態でなければsettings.pyのLOGIN_URLにリダイレクトされる
@method_decorator(login_required, name='dispatch')

class CreatePaintView(CreateView):
    '''イラストページのビュー
    PhotoPostFormで定義されているモデルとフィールドと連携して投稿データをデータベースに登録する'''
    form_class=PaintPostForm
    template_name="print_post.html"
    success_url=reverse_lazy('print:prin_post_done')
    
    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーライド
        
        フォームのバリデーションを通過したときに呼ばれる
        フォームデータの登録をここで行う'''
        # commit=FalseにしてPOSTされたデータを取得
        postdata=form.save(commit=False)
        # 投稿ユーザのidを取得してモデルのuserフィールドに格納
        postdata.user=self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    '''投稿完了ページのビュー'''
    template_name='prin_post_success.html'
    

class CategoryView(ListView):
    '''カテゴリの投稿一覧ページのビュー'''
    template_name='index.html'
    paginate_by=12
    
    def get_queryset(self):
        '''クエリを実行'''
        category_id=self.kwargs['category']
        categories=PaintPost.objects.filter(category=category_id).order_by('-posted_at')
        return categories

class UserView(ListView):
    '''ユーザーの投稿一覧のビュー'''
    template_name='index.html'
    paginate_by=12
    def get_queryset(self):
        '''クエリを実行'''
        user_id=self.kwargs['user']
        user_list=PaintPost.objects.filter(user=user_id).order_by('-posted_at')
        return user_list

class DetailView(DetailView):
    '''詳細ページのビュー'''
    template_name='detail.html'
    model=PaintPost
    context_object_name = 'record'

class MypageView(ListView):
    '''マイページのビュー'''
    template_name="mypage.html"
    paginate_by=12
    def get_queryset(self):
        '''クエリを実行する'''
        queryset=PaintPost.objects.filter(user=self.request.user).order_by('-posted_at')
        return queryset

class ContactView(FormView):
    '''お問い合わせページのビュー'''
    template_name='contact.html'
    form_class=ContactForm
    success_url=reverse_lazy('print:contact')
    
    def form_valid(self, form):
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        title=form.cleaned_data['title']
        message=form.cleaned_data['message']
        subject='お問い合わせ:{}'.format(title)
        message = \
            '送信者名: {0}\nメールアドレス: {1}\n タイトル:{2}\n メッセージ：\n{3}'.format(name, email, title, message)
        # メールの送信元のアドレス
        from_email = 'tky2302040@stu.o-hara.ac.jp'
        # 送信先のメールアドレス
        to_list = ['tky2302040@stu.o-hara.ac.jp']
        message=EmailMessage(subject=subject,
                               body=message,
                               from_email=from_email,
                               to=to_list,
                               )
        message.send()
        messages.success(
            self.request, 'お問い合わせは正常に送信されました。'
        )
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    '''レコードの削除を行う'''
    model=PaintPost
    template_name='post_delete.html'
    success_url=reverse_lazy('print:mypage')
    
    def delete(self, request, *args, **kwargs):
        '''レコードの削除を行う'''
        return super().delete(request, *args, **kwargs)
            





from django.shortcuts import render

from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404

from .forms import CommentPostForm
from .models import CommentPost
from print.models import PaintPost
# Create your views here.

@method_decorator(login_required, name='dispatch')
class CerateCommentView(CreateView):
    '''コメント投稿ページのビュー'''
    form_class=CommentPostForm
    template_name='comment_post.html'
    success_url=reverse_lazy('comment:comment_done')
    
    def form_valid(self, form): #  コメントのサーバー保存の参考:https://denno-sekai.com/django-comment/
        '''CreateViewクラスのform_valid()をオーバーライド'''
        comment_id=self.kwargs['post_id']
        c_id=get_object_or_404(PaintPost, pk=comment_id)
        postdata=form.save(commit=False)
        postdata.contact_id=c_id
        postdata.user=self.request.user
        postdata.save()
        return super().form_valid(form)

class CommentSuccessView(TemplateView):
    '''投稿完了ページのビュー'''
    template_name='comment_success.html'

class CommentListView(ListView):
    '''コメント一覧のビュー'''
    template_name='comments.html'
    model = CommentPost
    paginate_by=12
    def get_queryset(self):
        post_id=self.kwargs['post_id']
        queryset=CommentPost.objects.filter(contact_id=post_id).order_by('-posted_at')
        return queryset
      

    








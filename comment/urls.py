from django.urls import path
from . import views

app_name='comment'

urlpatterns = [
    path('comments/<int:post_id>', views.CommentListView.as_view(), name='comment_list'),
    path('comment_post/<int:post_id>', views.CerateCommentView.as_view(), name='comment_post'),
    path('comment_post_done/', views.CommentSuccessView.as_view(), name='comment_done')
]


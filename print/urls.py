from django.urls import path
from . import views

app_name='print'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    
    path('post/', views.CreatePaintView.as_view(), name='post'),
    path('post_done/', views.PostSuccessView.as_view(), name='prin_post_done'),
    path('posts/<int:category>', views.CategoryView.as_view(), name='prints_cat'),
    path('user-list/<int:user>', views.UserView.as_view(), name='user_list'),
    path('paint-detail/<int:pk>', views.DetailView.as_view(), name='print_detail'),
    path('mypage/', views.MypageView.as_view(), name='mypage'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('paint/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),        
]

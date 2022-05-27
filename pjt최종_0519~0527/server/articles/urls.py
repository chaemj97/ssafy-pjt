from django.urls import path
from . import views

app_name='articles'

urlpatterns = [ 
 path('',views.article_list), # 리스트, 생성
 path('<int:article_pk>/',views.article_detail), # 단일 읽기, update,delete
 path('<int:article_pk>/like/',views.article_like),
 path('comments/',views.comment_list),
 path('<int:article_pk>/comments/<int:comment_pk>/',views.comment_detail),
 path('<int:article_pk>/comments/',views.comment_create), # 댓글 생성
 
]

from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    # 전체 댓글 조회
    path('comments/', views.comment_list),
    # 상세 댓글 조회, 수정, 삭제
    path('comments/<int:comment_pk>/', views.comment_detail),
    # 댓글 생성
    path('articles/<int:article_pk>/comments/', views.comment_create),

]

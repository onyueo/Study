from django.urls import path
from . import views


urlpatterns = [
    path('musics/', views.music_list),
    path('musics/<int:music_pk>/', views.music_detail),
    # 전체 댓글 조회
    path('comments/', views.commnet_list),
    # 상세 댓글 조회, 수정, 삭제
    path('comments/<int:comment_pk>/', views.commnet_detail),
    # 댓글 조회, 생성
    path('music/<int:music_pk>/comments/', views.comment_create),
    
]

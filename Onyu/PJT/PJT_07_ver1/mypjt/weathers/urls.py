from django.urls import path, include
from . import views


urlpatterns = [
    # 1. 날씨 API 테스트
    path('', views.index),
    # 2. 서울의 5일치 예보 데이터 확인
    # 3. 예보 데이터 충 원하는 데이터만 DB에 저장
    path('save-data/', views.save_data),
    # 4. 저장된 데이터 전체 조회
    path('list-data/', views.list_data),
    # 5. 특정 조건 데이터 확인 : 섭씨 30도가 넘는 시간대 조회
    path('hot-weathers/', views.hot_weathers),
]

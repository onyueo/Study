from django.urls import path
from . import views

app_name = 'test_app'

urlpatterns = [
    path('A/', views.csv_to_df),
    path('B/', views.handle_null),
    path('C/', views.age_avg),
    path('D/', views.age_avg2),
    # D 는 Locust 를 활용한 알고리즘 성능 측정 
    # README.md에 총 접속자 동시 접속자 평균 RPS 응답시간 기록
]

from django.urls import path
from . import views

app_name="movies"
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:moive_pk>/', views.detail, name='detail'),
    path('update/<int:moive_pk>/', views.create, name='create'),
    path('delete/<int:moive_pk>/', views.delete, name='delete'),
    path('comments/<int:comment_pk>/', views.comments_create, name='comments_create'),
    # path('<int:moive_pk>/delete/<int:comment_pk>/', views.comments_delete, name='comments_delete'),
    # path('')

]


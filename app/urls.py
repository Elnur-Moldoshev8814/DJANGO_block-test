from django.urls import path, include

from . import views

urlpatterns = [
    path('author-list/', views.author_list),
    path('article-list/', views.article_list),
    path('author-detail/<str:login>/', views.author_detail),
    path('article-detail/<str:title>/', views.article_detail)
]

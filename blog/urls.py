from django.urls import path
from .views import index, article_detail, article_list, category

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('list/', article_list, name='list'),
    path('category/', category, name='category'),
    path('detail/<int:pk>/', article_detail, name='detail'),
]
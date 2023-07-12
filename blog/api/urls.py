from django.urls import path
from .views import (
    CategoryListCreateAPIView,
    CategoryRUDView,
    TagListCreateAPIView,
    TagRUDView,
    SubContentListCreateView,
    SubContentImageListCreateView,
    ArticleListCreateView,
    CommentListCreateAPIView
)


urlpatterns = [
    path('category/list-create/', CategoryListCreateAPIView.as_view()),
    path('category/rud/<int:pk>/', CategoryRUDView.as_view()),
    path('tag/list-create/', TagListCreateAPIView.as_view()),
    path('tag/rud/<int:pk>/', TagRUDView.as_view()),
    path('sub/content/list-create/', SubContentListCreateView.as_view()),
    path('sub/content/image/list-create/', SubContentImageListCreateView.as_view()),
    path('article/list-create/', ArticleListCreateView.as_view()),
    path('comment/list-create/', CommentListCreateAPIView.as_view())
]

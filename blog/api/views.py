from rest_framework import generics, permissions
from .serializers import CategorySerializer, TagSerializer, SubContentSerializer, SubContentImageSerializer, ArticleGetSerializer, ArticlePostSerializer, CommentSerializer
from ..models import Category, Tag, SubContent, SubContentImage, Article, Comment
from .permissions import IsAdminUserOrReadOnly, IsOwnerOrReadOnly


# Category view
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]


# Tag view
class TagListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class SubContentListCreateView(generics.ListCreateAPIView):
    queryset = SubContent.objects.all()
    serializer_class = SubContentSerializer


class SubContentImageListCreateView(generics.ListCreateAPIView):
    queryset = SubContentImage.objects.all()
    serializer_class = SubContentImageSerializer


class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGetSerializer
        return ArticlePostSerializer


class ArticleRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ArticleGetSerializer
        return ArticlePostSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset()
        article_id = self.kwargs.get('article_id')
        if article_id:
            qs = qs.filter(article_id=article_id)
            return qs
        return []

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx['article_id'] = self.kwargs.get('article_id')
        return ctx





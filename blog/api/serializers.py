from rest_framework import serializers
from ..models import Category, Tag, Article, SubContent, SubContentImage, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class MineSubContentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubContentImage
        fields = ['id', 'content', 'images', 'is_wide']


class MineSubContentSerializer(serializers.ModelSerializer):
    subcontent_image = MineSubContentImageSerializer(read_only=True)

    class Meta:
        model = SubContent
        fields = ['id', 'sub_content', 'subcontent_image']


class ArticleGetSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    Sub_Content = MineSubContentSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'image', 'description', 'Sub_Content','category', 'tags', 'created_date']


class SubContentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubContentImage
        fields = ['id', 'content', 'images', 'is_wide']


class SubContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubContent
        fields = ['id', 'article', 'sub_content']
        extra_kwargs = {
            'article': {'required': False}
        }

        def create(self, validated_data):
            article_id = self.context['article_id']
            content = validated_data.get('content')
            instance = SubContent.objects.create(article_id=article_id, content=content)
            return instance


class ArticlePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'image', 'description', 'category', 'tags', 'created_date']
        extra_kwargs = {
            'article': {'read_only': True}
        }

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user.profile
        instance = super().create(validated_data)
        instance.author = author
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'article', 'description', 'created_date']

    def create(self, validated_data):
        request = self.context['request']
        article_id = self.context['article_id']
        author_id = request.user.profile.id
        description = validated_data.get('description')
        instance = Comment.objects.create(article_id=article_id, author_id=author_id, description=description)
        return instance


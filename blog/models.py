from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=112)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=112)

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey("profiles.Profile", on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=112)
    category = models.ForeignKey(Category, on_delete=models.CASCADE )
    image = models.ImageField(upload_to='articles/')
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SubContent(models.Model):
    article = models.OneToOneField(Article, on_delete=models.CASCADE, related_name='subcontent')
    sub_content = models.TextField()


class SubContentImage(models.Model):
    content = models.ForeignKey(SubContent, on_delete=models.CASCADE, related_name='subcontentimage')
    images = models.ImageField(upload_to='articles/')
    is_wide = models.BooleanField()


class Comment(models.Model):
    author = models.ForeignKey('profiles.Profile', on_delete=models.SET_NULL, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.author.user.get_full_name():
            return f"{self.author.user.get_full_name()}'s comment"
        return f"{self.author.user.get_full_name()}'s comment"

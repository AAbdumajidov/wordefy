from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Article, Tag, Category
from .forms import CommentForm


def index(request):
    articles = Article.objects.order_by('-id')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    search = request.GET.get('search')
    if cat:
        articles = articles.filter(category__title__exact=cat)
    if tag:
        articles = articles.filter(tags__title__exact=tag)
    if search:
        articles = articles.filter(title__icontains=search)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 2)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(3)
    ctx = {
        'object_list': page_obj,
        'tags': tags,
        'categories': categories,
    }
    return render(request, 'wordify/index.html', ctx)


def category(request):
    articles = Article.objects.order_by('-id')
    tags = Tag.objects.all()
    categories = Category.objects.all()

    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    cats = request.GET.get('cat')
    if cat:
        articles = articles.filter(category__title__exact=cat)
    if tag:
        articles = articles.filter(tags__title__exact=tag)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(3)
    ctx = {
        'object_list': page_obj,
        'tags': tags,
        'categories': categories,
        'cats':cats

    }
    return render(request, 'wordify/category.html', ctx)


def article_list(request):
    articles = Article.objects.all().order_by('-id')
    tagis = Tag.objects.all()
    categories = Category.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    cats = request.GET.get('cat')
    search = request.GET.get('search')
    if cat:
        articles = articles.filter(category__title__exact=cat)
    if tag:
        articles = articles.filter(tags__title__exact=tag)
    if search:
        articles = articles.filter(title__icontains=search)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(articles, 2)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(3)
    ctx = {
        'object_list': page_obj,
        'tags': tagis,
        'categories': categories,
        'cat': cat,
        'cats': cats,

    }
    return render(request, 'wordify/category.html', ctx)


def article_detail(request, pk):
    article = get_object_or_404(Article, id=pk)
    tag = Tag.objects.all()
    categories = Category.objects.all()
    form = CommentForm()
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(reverse('accaunt:login'))
        form = CommentForm(data=request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author_id = request.user.profile.id
            obj.article_id = article.id
            obj.save()
            return redirect('.')
    ctx = {
        'object': article,
        'form': form,
        'tags': tag,
        'categories': categories,
    }
    return render(request, 'wordify/blog-single.html', ctx)

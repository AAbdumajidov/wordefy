from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from blog.models import Article, Tag, Category
from .models import Contact
from .forms import ContactForm


def contact(request):
    form = ContactForm(request.POST or None)
    articles = Article.objects.all().order_by('-id')
    tags = Tag.objects.all()
    categories = Category.objects.all()
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
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
        
    if form.is_valid():
        form.save()
        return redirect('contact:index')
    ctx = {
        'object_list': page_obj,
        "form": form,
        'tags': tags,
        'categories': categories,
    }
    return render(request, 'wordify/contact.html', ctx)
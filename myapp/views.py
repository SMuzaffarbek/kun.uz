from django.shortcuts import render, HttpResponse
from .models import News, Category

def category(request):
    categories = Category.objects.all()
    return  {'categories': categories}

def category_news(request, slug):
    category = Category.objects.get(slug=slug)
    news = News.objects.filter(category = category)
    context = {
        'news': news,
        'category':category,
    }
    return render(request, 'category_new.html', context)

def home(request):
    news = News.objects.all()
    context = {
        'news':news,
    }
    return render(request, 'home.html', context)

def new_detail(request, slug):
    new = News.objects.get(slug=slug)
    news_last = News.objects.all().order_by('-created_at')[:10]
    news_category = News.objects.filter(category=new.category)[:10]
    new.view_news += 1
    new.save()

    context = {
        'new':new,
        'news_last':news_last,
        'news_category':news_category,
    }
    return render(request, 'detail.html', context)
from django.shortcuts import render
from .models import News, Category

# Create your views here.
def home(request):
    first_news = News.objects.last() # displayes the frst main news 
    three_news = News.objects.all()[1:4] # displayes the three news by skipping the first news.
    three_categories = Category.objects.all()[0:3] # displayes the three news by skipping the first categories.
# rendering the data in the templates 
    return render(request, 'home.html',{
        'first_news': first_news,
        'three_news': three_news,
        'three_categories': three_categories
    })


# Fetching the  All news 
def all_news(request):
    all_news = News.objects.all()
    return render(request, 'all-news.html',{
        'all_news': all_news
    })

# detail Page
def detail(request, id):
    news = News.objects.get(pk=id)
    category = Category.objects.get(id=news.category.id)
    rel_news = News.objects.filter(category=category).exclude(id=id)
    return render(request, 'detail.html',{
        'news': news, 
        'related_news': rel_news
    })

# displaying the category 


def all_category(request):
    cats = Category.objects.all()
    return render(request, 'category.html',{
        'cats': cats
    })

    
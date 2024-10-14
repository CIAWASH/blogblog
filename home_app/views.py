from django.shortcuts import render
from blog.models import Article
from django.urls import reverse

# Create your views here.

def home(request):
    articles = Article.objects.all()
    # articles = Article.custom_manager.all()
    # recent_articles = Article.objects.all()[:2]
    recent_articles = Article.objects.all().order_by('-created', '-updated')[:3]
    return render(request, "home_app/index.html", {"articles": articles}) #{"articles": articles, "recent_articles": recent_articles})
    

def sidebar(request):
    data = {'name': 'Ciawash'}
    return render(request, 'includes/sidebar.html', context=data)


def about(request):
    return render(request, "home_app/about.html", {})
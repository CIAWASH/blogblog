from blog.models import Article, Category



def recent_articles(request):
    recent_articles = Article.objects.order_by('-created')
    # We could have written this: Article.objects.all.order_by('-created')
    categories = Category.objects.all()

    return {"recent_articles": recent_articles, "categories": categories}
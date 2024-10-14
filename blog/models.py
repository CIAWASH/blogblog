from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from datetime import datetime

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(status=True)


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    category = models.ManyToManyField(Category, related_name="articles")
    title = models.CharField(max_length=70, unique_for_date="pub_date")
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField(default=timezone.now())
    floatfield = models.FloatField(default=1)
    myfile = models.FileField(upload_to='test', null=True)
    status = models.BooleanField(default=True)
    published = models.BooleanField(default=True)
    slug = models.SlugField(blank=True, unique=True)
    objects = models.Manager()
    custom_manager = ArticleManager()

    # is_published = models.DurationField(default=timezone.timedelta(days=23, hours=21, minutes=43, seconds=54))

    # class Meta:
    #     ordering = ('-updated', '-created',) # ended with a comma to tell django it's a tuple.
    #     # It could also be : ['-created']
    #     verbose_name = "post" # So 'post' is used instead of the word 'article' in the control panel
    #     verbose_name_plural = "stories"

    # def save(self, force_insert: False, force_update: False, using: None, update_fields: None):
    #     self.slug = slugify(self.title)
    #     super(Article, self).save(force_insert, force_update, using, update_fields)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={"slug": self.slug}) #The value may be:articles/detail/3              The previous was kwargs={title": self.title}
        # return reverse("blog:article_detail", args=[self.id]) 
        # We could have used kwargs instead of args:  kwargs={'pk': self.id}

    def __str__(self):
        return f"{self.title} - {self.body[:30]}"
    

    class Meta:
        ordering = ("-created",)



# From article to comments: rabeteye maaxus: article.comments.all()

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments') # from comment to article: comment.article
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.body[:50]







        
class Message(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    email = models.EmailField()
    age = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    date = models.DateTimeField(default=timezone.now())
    
  
    
    def __str__(self):
        return self.title         



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes", verbose_name="کاربر")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="likes", verbose_name="مقاله")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.article.title}"
    
    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "لایک ها"
        ordering = ('-created_at',)
from typing import Any, Optional
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from blog.models import Article, Category, Comment, Message, Like
from django.core.paginator import Paginator
from .forms import ContactUsForm, MessageForm
from django.views.generic.base import View, TemplateView, RedirectView
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView, ArchiveIndexView, YearArchiveView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse

# Create your views here.


def article_detail(request, slug):
    # article = Article.objects.get(id=pk)
    article = get_object_or_404(Article, slug=slug) #The previous version was title=title
    if request.method == 'POST':
        body = request.POST.get('body')
        Comment.objects.create(body=body, article=article, user=request.user)
    return render(request, "blog/article_details.html", {"article": article})


#def article_detail(request, pk):
    # article = Article.objects.get(id=pk)
    # article = get_object_or_404(Article, id=pk)
    # return render(request, "blog/article_details.html", {"article": article})


def article_list(request):  
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    objects_list = paginator.get_page(page_number)
    return render(request, "blog/articles_list.html", {"articles": objects_list})


def category_detail(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    # articles = category.article_set.all() We changed the name in the Article class to "articles"
    articles = category.articles.all()
    return render(request, "blog/articles_list.html", {"articles": articles})



def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    objects_list = paginator.get_page(page_number)
    return render(request, "blog/articles_list.html", {"articles": objects_list})



def contactus(request):
    if request.method == 'POST':
        
        form = MessageForm(data=request.POST)
        if form.is_valid():
            # return redirect('home_app:main') We wanna stay in the same page.
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            email = form.cleaned_data['email']
            Message.objects.create(title=title, text=text, email=email)
            # form.save() Alternative to writing all fields

    else:
        form = MessageForm()
    return render(request, "blog/contact_us.html", {'form': form})




class TestBaseView(View):
    name = "Ciawash"
    def get(self, request):
        return HttpResponse(self.name)
    


class HelloToAli(TestBaseView):
    name = "ali"



class HelloToKarim(TestBaseView):
    name = "karim"



# class ListView(View): We no longer need it because we imported the whole package
#     queryset = None
#     template_name = None

#     def get(self, request):
#         return render(request, self.template_name, {'object_list': self.queryset})
    


# class ArticleList(ListView):
#     queryset = Article.objects.all()
#     template_name = "blog/articles_list.html"



class UserList(ListView):
    queryset = User.objects.all()
    template_name = "blog/user_list.html"



class ArticleList(TemplateView):
    model = Article
    # context_object_name = "articles" It must be converted to object_list or this attribute could be removed. Watch the relevant video!
    paginate_by = 1
    template_name = "blog/articles_list2.html"
    queryset = Article.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Article.objects.all() 
        return context
    

class HomePageRedirect(RedirectView):
    # url = "/articles/list" We could also use the pattern_name:
    pattern_name = "blog:article_detail"
    permanent = False
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        print(self.request.user.username)
        return super().get_redirect_url(*args, **kwargs)
    



class ContactUsView(FormView):
    template_name = "blog/contact_us.html"
    form_class = MessageForm
    # success_url = "/"  We could have used this:
    # success_url = reverse(home_app:main) But because of bookmark 4, we use this:
    success_url = reverse_lazy("home_app:main")

    def form_valid(self, form):
        form_data = form.cleaned_data
        # Message.objects.create(title=form_data["title"]) Instead we use this:
        Message.objects.create(**form_data)
        return super().form_valid(form)



class MessageView(CreateView):
    model = Message
    # fields = ('title', 'text') Instead of manually typing all fields, we can use this:
    # fields = "__all__"
    fields = ('title', 'text', 'date', 'age')
    success_url = reverse_lazy('home_app:main')
    # template_name = "blog" As the name rules are followed, we don't need this

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["messages"] = Message.objects.all() 
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.email = self.request.user.email
        instance.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        print(self.object)
        return super(MessageView).get_success_url()
    


class MessagesListView(ListView):
    model = Message


class MessageUpdateView(UpdateView):
    model = Message
    fields = ('title', 'text', 'age') # Fields that you'd like to change
    template_name_suffix = "_update_form" # We could also have used this:
    # template_name = "blog/message_update_form.html"
    success_url = reverse_lazy("blog:message_list")



class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("blog:message_list")



class ArchiveIndexArticleView(ArchiveIndexView):
    model = Article
    date_field = "updated"



class YearArchiveArticleView(YearArchiveView):
    model = Article
    date_field = "pub_date"
    make_object_list = True
    allow_future = True
    # template_name = "blog/article_archive_year.html"


    

def like(request, slug, pk):
    try:
        like = Like.objects.get(article__slug=slug, user_id=request.user.id)
        like.delete()
        return JsonResponse({"response": "unliked"})

    except:
        Like.objects.create(article_id=pk, user_id=request.user.id) 
        return JsonResponse({"response": "liked"})

   




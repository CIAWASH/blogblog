from django.urls import path
from . import views

# /articles/
app_name = "blog"
urlpatterns = [
    path('detail/<slug:slug>', views.article_detail, name="article_detail"),
    path('list', views.article_list, name="articles_list"),
    path('list2', views.ArticleList.as_view(), name="articles_list2"),
    path('category/<int:pk>', views.category_detail, name="category_detail"),
    path('search', views.search, name="search_articles"),
    path('contactus', views.contactus, name="contact_us"),
    path('testbase', views.TestBaseView.as_view(), name="test_base"),
    path('ali', views.HelloToAli.as_view(), name="test_ali"),
    path('karim', views.HelloToKarim.as_view(), name="test_karim"),
    path('users', views.UserList.as_view(), name="user_list"),
    path('red/<slug:slug>', views.HomePageRedirect.as_view(), name="redirect"),
    path('messages', views.MessageView.as_view(), name="messages"),
    path('message_list', views.MessagesListView.as_view(), name="message_list"),
    path('message/edit/<int:pk>', views.MessageUpdateView.as_view(), name="message_edit"),
    path('message/delete/<int:pk>', views.MessageDeleteView.as_view(), name="message_delete"),
    path('archive', views.ArchiveIndexArticleView.as_view(), name="archive"),
    path('archive/<int:year>', views.YearArchiveArticleView.as_view(), name="archive_year"),
    path('like/<slug:slug>/<int:pk>', views.like, name="like"),
]

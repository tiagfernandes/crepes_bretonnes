from django.urls import path, re_path
from . import views

urlpatterns = [
    path('accueil', views.home, name="home"),
    # path('articles/<str:tag>', views.list_articles_by_tag),
    # re_path(r'^articles/(?P<month>\d{2})/(?P<year>\d{4})', views.list_articles),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
    path('pourcentage/<int:nombre1>/<int:nombre2>/', views.pourcentage),
    path('', views.accueil, name='accueil'),
    path('article/<int:id>-<slug:slug>', views.lire, name='lire'),
    path('contact/', views.contact, name='contact'),
    path('article/new', views.article_new, name='article_new'),
]

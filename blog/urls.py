from django.urls import path, re_path
from . import views

urlpatterns = [
    path('accueil', views.home),
    path('article/<int:id_article>', views.view_article),
    path('articles/<str:tag>', views.list_articles_by_tag),
    re_path(r'^articles/(?P<month>\d{2})/(?P<year>\d{4})', views.list_articles),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition)
]

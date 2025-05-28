from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('articles/category/<slug:category_slug>/', views.ArticleListView.as_view(), name='articles_by_category'),
    path('articles/<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('projects/', views.ProjectListView.as_view(), name='projects'),
    path('about/', views.about, name='about'),
] 
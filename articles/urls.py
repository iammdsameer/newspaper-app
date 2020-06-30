from django.urls import path
from .views import ArticleListView, ArticleUpdateView, ArticleDetailView, ArticleDeleteView, ArticleCreateView

urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='edit_article'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='view_article'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='delete_article'),
    path('create/', ArticleCreateView.as_view(), name='create_article'),
]
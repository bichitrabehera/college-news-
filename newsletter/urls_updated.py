from django.urls import path
from .views import submit_article, home, approve_article, admin_article_list, render_static_html, article_detail_view  # Import the new view

urlpatterns = [
    path('', home, name='home'),
    path('submit/', submit_article, name='submit_article'),
    path('admin/articles/', admin_article_list, name='admin_article_list'),
    path('admin/articles/approve/<int:article_id>/', approve_article, name='approve_article'),
    path('article/<int:article_id>/', article_detail_view, name='article_detail'),  # New URL pattern for article detail
]

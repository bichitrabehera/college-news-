from django.urls import path
from .views import submit_article, home, approve_article, admin_article_list

urlpatterns = [
    path('', home, name='home'),
    path('submit/', submit_article, name='submit_article'),
    path('admin/articles/', admin_article_list, name='admin_article_list'),
    path('admin/articles/approve/<int:article_id>/', approve_article, name='approve_article'),
]
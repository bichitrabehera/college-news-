from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm  

def home(request):
    articles = Article.objects.filter(is_approved=True)  # Only show approved articles
    return render(request, 'newsletter/home.html', {'articles': articles})
def submit_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.is_approved = False  
            article.save()
            return redirect('home')  # Redirect to home after submission
    else:
        form = ArticleForm()
    return render(request, 'newsletter/submit_article.html', {'form': form})
def render_static_html(request):
    return render(request, 'newsletter/submit_article.html') 

def approve_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.is_approved = True  # Approve the article
    article.save()
    return redirect('admin_article_list')  # Redirect to admin list after approval

def admin_article_list(request):
    articles = Article.objects.filter(is_approved=False)  # List unapproved articles
    return render(request, 'newsletter/admin_article_list.html', {'articles': articles})

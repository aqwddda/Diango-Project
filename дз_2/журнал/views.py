from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import User, Article

class UserInterface:
    @staticmethod
    def login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'login.html', {'error': 'Invalid login credentials'})
        else:
            return render(request, 'login.html')

    @staticmethod
    def register(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'register.html')

    @staticmethod 
    def index(request):
        articles = Article.objects.all()
        return render(request, 'index.html', {'title': 'научный_электронный_журнал', 'articles': articles})
        
class SearchArticle:
    @staticmethod
    def search_title(request):
        if request.method == 'POST':
            title = request.POST['title']
            articles = Article.objects.filter(title__icontains=title)
            return render(request, 'search_results.html', {'articles': articles})
        else:
            return render(request, 'search_title.html')
        
    @staticmethod
    def article_detail(request, article_id):
        article = Article.objects.get(id=article_id)
        context = {
            'article': article
        }
        return render(request, 'article_detail.html', context)




from django.urls import path
from . import views

app_name = 'журнал'

urlpatterns = [
    path('', views.UserInterface.index, name='index'), 
    path('login/', views.UserInterface.login, name='login'),
    path('register/', views.UserInterface.register, name='register'),
    path('search_title/', views.SearchArticle.search_title, name='search_title'),
    path('<int:article_id>/', views.SearchArticle.article_detail, name='article_detail'),
]
from django.urls import path
from . import views_search

urlpatterns = [
    path('', views_search.Accueil_de_recherche, name='Accueil_de_recherche'),
    path('index', views_search.index, name='index'),
    path('barred_search', views_search.barred_search, name='barred_search'),
]
from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    # /movies/?page=1  => HTML
    path('', views.index, name='index'),
    # /movies/ajax/?page=2  => JSON
    path('ajax/', views.ajax, name='ajax'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('recommended/', views.recommended, name='recommended'),
]

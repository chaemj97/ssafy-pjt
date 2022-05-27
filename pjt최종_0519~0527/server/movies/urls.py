from django.urls import path
from . import views

app_name='movies'

urlpatterns = [
    path('',views.movie_list),
    path('topten/', views.movie_topten),
    path('genre/', views.movie_genre),
    path('time/', views.movie_time),
    path('<int:movie_pk>/',views.movie_detail),
    path('<int:movie_pk>/like/', views.movie_like),
    path('<int:movie_pk>/reviews/',views.create_review),
    path('<int:movie_pk>/reviews/<int:review_pk>/',views.review_detail),
    path('birth/', views.movie_birth),
    path('md/', views.md_pick),
]

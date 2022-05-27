from rest_framework import serializers
from django.contrib.auth import get_user_model
from articles.models import Article
from movies.models import Movie

class ProfileSerializer(serializers.ModelSerializer):
    class MovieSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('pk','title','poster_path',)
    like_movies = MovieSerializer(many=True)

    class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
            model = Article
            fields= ('pk', 'title')
    like_articles = ArticleSerializer(many=True)
    article_set = ArticleSerializer(many=True)
    
    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'like_movies', 'like_articles', 'article_set')
    
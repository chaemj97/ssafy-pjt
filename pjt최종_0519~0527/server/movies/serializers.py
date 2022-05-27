from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie,Review, Genre

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('pk', 'title','poster_path',)

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('pk', 'title',)

User = get_user_model()

class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    movie =MovieListSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('pk','user','score','movie',)

class MovieDetailSerializer(serializers.ModelSerializer):
    class GenreSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'
    genres = GenreSerializer(many=True, read_only=True)

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username',)
            
    review_set = ReviewSerializer(many=True,read_only = True)
    like_users = UserSerializer(read_only=True, many=True)
    
    class Meta:
        model = Movie
        fields = ('pk','title','overview','release_date','poster_path',
        'genres','vote_count','vote_average','like_users','review_set')



    
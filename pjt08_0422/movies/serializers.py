from rest_framework import serializers
from .models import Actor,Movie,Review


class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name',)

class Actor2Serializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('name',)

class Movie1Serializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title',)

class ActorSerializer(serializers.ModelSerializer):
    movies = Movie1Serializer(many=True, read_only = True)
    class Meta:
        model = Actor
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview',)

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content',)

class MovieSerializer(serializers.ModelSerializer):
    review_set = ReviewListSerializer(many=True,read_only = True)
    actors = Actor2Serializer(many=True,read_only = True)
    class Meta:
        model = Movie

        # 다 적기
        fields = (
            'id', 'actors','review_set',
            'title','overview','release_date',
            'poster_path'
        )



class ReviewSerializer(serializers.ModelSerializer):
    movie = Movie1Serializer(read_only = True)
    class Meta:
        model = Review
        fields = '__all__'     
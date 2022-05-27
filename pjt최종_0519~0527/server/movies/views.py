from django.http import JsonResponse
from django.shortcuts import get_list_or_404,get_object_or_404,render
from .models import Movie,Review
from rest_framework.decorators import api_view
from .serializers import MovieDetailSerializer,ReviewSerializer,MovieSerializer
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

@ api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@ api_view(['GET'])
def movie_topten(request):
    movies = Movie.objects.order_by('-vote_average')[:10]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)



@ api_view(['GET'])
def movie_detail(request,movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user = request.user
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
    else:
        movie.like_users.add(user)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def create_review(request, movie_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        pre_point = movie.vote_average * movie.vote_count
        point = pre_point + float(request.data.get('score'))
        count = movie.vote_count + 1
        new_vote_average = round(point/count, 2)

        movie.vote_average = new_vote_average
        movie.vote_count = count
        movie.save()
        serializer.save(movie=movie, user=user)
        review = movie.review_set.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)

@ api_view(['GET','PUT','DELETE'])
def review_detail(request, movie_pk, review_pk):
    # article 조회, 생성, 삭제
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review,pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review,data=request.data)
        if serializer.is_valid(raise_exception=True):
            pre_point = movie.vote_average * movie.vote_count
            point = pre_point - review.score + float(request.data.get('score'))
            count = movie.vote_count
            new_vote_average = round(point/count, 2)
            movie.vote_average = new_vote_average
            movie.vote_count = count
            movie.save()
            serializer.save(movie=movie, user=request.user)
            review = movie.review_set.all()
            # print(review)
            serializer = ReviewSerializer(review, many=True)
            return Response(serializer.data)
    elif request.method == 'DELETE':
        pre_point = movie.vote_average * movie.vote_count
        point = pre_point - review.score
        count = movie.vote_count - 1
        new_vote_average = round(point/count, 2)
        movie.vote_average = new_vote_average
        movie.vote_count = count
        movie.save()
        review.delete()
        review = movie.review_set.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)

@ api_view(['GET'])
def movie_genre(request):
    romance = Movie.objects.filter(genres=10749)
    fantasy = Movie.objects.filter(genres=14)
    horror = Movie.objects.filter(genres=27)
    action = Movie.objects.filter(genres=28)
    comedy = Movie.objects.filter(genres=35)
    animation = Movie.objects.filter(genres=16)
    thriller = Movie.objects.filter(genres=53)
    family = Movie.objects.filter(genres=10751)
    data = {
        'ROMANCE': MovieSerializer(romance, many=True).data,
        'FANTASY': MovieSerializer(fantasy, many=True).data,
        'HORROR': MovieSerializer(horror, many=True).data,
        'ACTION': MovieSerializer(action, many=True).data,
        'COMEDY': MovieSerializer(comedy, many=True).data,
        'ANIMATION': MovieSerializer(animation, many=True).data,
        'THRILLER': MovieSerializer(thriller, many=True).data,
        'FAMILY': MovieSerializer(family, many=True).data,
    }
    return Response(data)

@ api_view(['GET'])
def movie_time(request):
    dawn = [27, 53, 80, 99, 9648, 10402, ]
    morning = [16, 18, 35, 10402, 10770, ]
    day = [12, 14, 28, 36, 37, 878, ]
    night = [18, 28, 35, 10749, 10751, 10770, ]
    dawn_movie = Movie.objects.filter(genres__in=dawn).distinct()
    morning_movie = Movie.objects.filter(genres__in=morning).distinct()
    day_movie = Movie.objects.filter(genres__in=day).distinct()
    night_movie = Movie.objects.filter(genres__in=night).distinct()
    now = datetime.now().time().hour
    if 0 <= now < 6:
        data = {
            '⭐ dawn': MovieSerializer(dawn_movie, many=True).data,
        }
    elif 6 <= now < 12:
        data = {
            '🌄 MORNING': MovieSerializer(morning_movie, many=True).data,
        }
    elif 12 <= now < 18:
        data = {
            "🌞 DAY": MovieSerializer(day_movie, many=True).data,
        }
    else:
        data = {
            '🌙 NIGHT': MovieSerializer(night_movie, many=True).data,
        }
    return Response(data)

@ api_view(['GET','POST'])
def movie_birth(request):
    # client가 날짜를 입력 = birthday
    if request.method == 'POST':
        month = request.data["birthday"][5:7]
        day = request.data["birthday"][8:]
        # server가 그 날짜에 개봉한 영화를 찾아
        movies = Movie.objects.filter(release_date__month = month, release_date__day = day)  
        # client에게 준다...
        serializer = MovieSerializer(movies,many=True)
        return Response(serializer.data)
    elif request.method == 'GET':
        pass

from django.db.models import Q

@api_view(['GET'])
def md_pick(request):
    first = Movie.objects.filter(Q(title="쇼생크 탈출")|Q(title='인터스텔라')|
        Q(title='인셉션')|Q(title='벤자민 버튼의 시간은 거꾸로 간다')|
        Q(title='포레스트 검프'))
    second = Movie.objects.filter(Q(title="수상한 그녀")|Q(title='인터스텔라')|
        Q(title='극한직업')|Q(title='오케이 마담')|
        Q(title='모가디슈'))
    third = Movie.objects.filter(Q(title="미쓰 와이프")|Q(title='엑시트')|
        Q(title='세상에서 가장 아름다운 이별')|Q(title='미녀는 괴로워')|
        Q(title='김종욱 찾기'))
    data = {
        'first':MovieSerializer(first, many=True).data,
        'second':MovieSerializer(second, many=True).data,
        'third':MovieSerializer(third, many=True).data
    }
    return Response(data)

    
from multiprocessing import context
from django.shortcuts import render
import requests
import random

# Create your views here.
def index(request):
    return render(request,'movies/index.html')
        
def reco(request,title):
    BASE_URL = 'http://api.themoviedb.org/3'
    path1 = '/search/movie'
    params1 = {
        'api_key' : '1b2024caa40beafad9a3a4e9073e7e88',
        'language' : 'ko',
        'query' : title
    }

    response1 = requests.get(BASE_URL+path1, params=params1)
    data1 = response1.json()
    
    if data1['results'] == []:
        return None
    
    movie_id = data1['results'][0]['id']
    # id 불렀음

    path2 = f'/movie/{movie_id}/recommendations'
    params2 = {
        'api_key' : '1b2024caa40beafad9a3a4e9073e7e88',
        'language' : 'ko'
    }
    response2 = requests.get(BASE_URL+path2, params=params2)
    data2 = response2.json()
    
    # 추천영화 
    if data2['results'] == []:
        return []
    else:
        result = []
        movie = random.sample(data2['results'],1)
        # 제목
        result.append(movie[0]['title'])
        # 줄거리
        result.append(movie[0]['overview'])
        # 개봉일
        result.append(movie[0]['release_date'])
        # 링크 연결
        result.append(movie[0]['id'])
        # 사진
        result.append(movie[0]['poster_path'])
        # 평점
        result.append(movie[0]['vote_average'])
    return result
def recommendations(request):
    result = reco(request,'쇼생크 탈출')
    context = {
        'title' : result[0],
        'overview' : result[1],
        'release_date' : result[2],
        'id' : result[3],
        'poster_path' : result[4],
        'vote_average' : result[5],
    }

    return render(request, 'movies/recommendations.html', context)
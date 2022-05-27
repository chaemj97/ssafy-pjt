# 목표 : 아래 형태를 만들고 싶음
# {
#     "model": "movies.genre",
#     "pk": 28,
#     "fields": {
#       "name": "액션"
#     }
#   },

import requests
from pprint import pprint
import json

BASE_URL = "https://api.themoviedb.org/3"

# 장르 Json 만들기

# URI는 특정 리소스를 식별하는 통합 자원 식별자(Uniform Resource Identifier)
# 각 장르 id의 의미
GENRE_LIST_URI = "/genre/movie/list"
genre_list = []
genre_params = {
    'api_key' : '1b2024caa40beafad9a3a4e9073e7e88',
    'language' : 'ko',
}
genre_response = requests.get(BASE_URL+GENRE_LIST_URI, params=genre_params)
genre_data = genre_response.json()

for data in genre_data["genres"]:
    my_genre = {
        "model": "movies.genre",
        "pk": data["id"],
        "fields": {
            "name": data["name"]
        },
    }
    genre_list.append(my_genre)
########################################################################


# Movie Json 만들기
MOVIE_LIST_URI = "/movie/popular"
movie_list = []
for num in range(1,31):
    movie_params = {
        'api_key' : '1b2024caa40beafad9a3a4e9073e7e88',
        'language' : 'ko',
        'page': num,
    }  
    movie_response = requests.get(BASE_URL+MOVIE_LIST_URI, params=movie_params)
    movie_data = movie_response.json()
    for data in movie_data["results"]:
        if data["release_date"]:
            my_movie = {
                    "model": "movies.movie",
                    "fields": {
                        "title": data["title"],
                        "overview": data["overview"],
                        "release_date": data["release_date"],
                        "poster_path": data["poster_path"],
                        "genres": data["genre_ids"],
                        "vote_count": data["vote_count"],
                        "vote_average": data["vote_average"],
                    }  
                }
            movie_list.append(my_movie)
        

with open('movies.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(movie_list, ensure_ascii=False))

with open('genres.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(genre_list, ensure_ascii=False))
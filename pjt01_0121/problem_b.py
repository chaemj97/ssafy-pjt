import json
from pprint import pprint


def movie_info(movie, genres):
    # 여기에 코드를 작성합니다.
  
    # 필요 정보 key 리스트로 작성
    lst = ['id','title','poster_path','vote_average','overview']
    dict_movie = {}
    # 필요 정보 key에 맞는 value를 딕셔너리에 추가
    for i in lst:
        dict_movie[i] = movie.get(i)

        # genre_ids를 genre_names로 변환해서 추가
        # genre_ids값과 genres의 id 값이 같다면 genres의 name 값을 genre_names 리스트에 추가
        genre_names = []
        for j in movie['genre_ids']:
            for k in range(len(genres)):
                if j == genres[k]['id']:
                    genre_names.append(genres[k]['name'])
        # genre_names를 딕셔너리에 추가
        dict_movie['genre_names'] = genre_names

    return dict_movie
    
    
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
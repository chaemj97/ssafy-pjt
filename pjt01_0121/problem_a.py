import json
from pprint import pprint


def movie_info(movie):
    # 여기에 코드를 작성합니다.

    # 필요 정보 key 리스트로 작성
    lst = ['id','title','poster_path','vote_average','overview','genre_ids']
    dict_movie = {}
    # 필요 정보 key에 맞는 value를 딕셔너리에 추가
    for i in lst:
        dict_movie[i] = movie.get(i)
        
    return dict_movie        
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
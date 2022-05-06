from audioop import reverse
import requests
from pprint import pprint


def ranking():
    pass 
    # 여기에 코드를 작성합니다.
    BASE_URL = 'http://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : '1b2024caa40beafad9a3a4e9073e7e88',
        'language' : 'ko'
    }
    response = requests.get(BASE_URL+path, params=params)
    data = response.json()

    data['results'].sort(key = lambda x: x['vote_average'],reverse =True)
    return data['results'][0:5]



if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화.
    """
    pprint(ranking())
    # => 영화정보 순서대로 출력

import requests
from pprint import pprint


def vote_average_movies():
    pass 
    # 여기에 코드를 작성합니다.
    BASE_URL = 'http://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key' : '1b2024caa40beafad9a3a4e9073e7e88',
        'language' : 'ko'
    }
    response = requests.get(BASE_URL+path, params=params)
    print(response.status_code,response.url)
    data = response.json()
    

    result = []
    for i in range(len(data['results'])): 
        if data['results'][i]['vote_average'] >= 8:
            result.append(data['results'][i]) 

    return result

if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    pprint(vote_average_movies())
    # => 영화정보 순서대로 출력

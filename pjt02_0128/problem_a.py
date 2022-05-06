import requests


def popular_count():
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

    return len(data['results'])


if __name__ == '__main__':
    """
    popular 영화목록의 개수 출력.
    """
    print(popular_count())
    # => 20

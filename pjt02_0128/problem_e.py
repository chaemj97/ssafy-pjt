import requests
from pprint import pprint


def credits(title):
    pass 
    # 여기에 코드를 작성합니다.
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

    path2 = f'/movie/{movie_id}/credits'
    params2 = {
        'api_key' : '1b2024caa40beafad9a3a4e9073e7e88',
        'language' : 'ko'
    }
    response2 = requests.get(BASE_URL+path2, params=params2)
    data2 = response2.json()
    print(response2.status_code, response2.url)

    result ={'cast': [] ,'crew': []}
    for i in range(10):
        result['cast'] += [data2['cast'][i]['name']]
    for j in range(len(data2['crew'])):
        if data2['crew'][j]['department'] == 'Directing':
            result['crew'] += [data2['crew'][j]['name']]


    return result

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록(cast)과 제작진(crew).
    영화 id검색에 실패할 경우 None.
    """
    pprint(credits('기생충'))
    # => {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # => None

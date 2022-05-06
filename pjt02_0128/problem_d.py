import requests
from pprint import pprint


def recommendation(title):
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
    print(response1.status_code,response1.url)
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
    print(response2.status_code,response2.url)
    data2 = response2.json()
    

# 추천영화목록 조회 했음
    if data2['results'] == []:
        return []
    else:
        result = []
        for i in range(len(data2['results'])):
          result.append(data2['results'][i]['title'])

    return result    
    

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록 구성.
    추천 영화가 없을 경우 [].
    영화 id검색에 실패할 경우 None.
    """
    pprint(recommendation('기생충'))
    # ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
    pprint(recommendation('그래비티'))
    # []  => 추천 영화 없음
    pprint(recommendation('검색할 수 없는 영화'))
    # => None

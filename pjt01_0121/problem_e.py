import json
from platform import release
from datetime import date


def dec_movies(movies):
    # 여기에 코드를 작성합니다. 

    # 개봉월이 12월이 영화들의 제목 리스트를 출력

    # 각각의 파일을 열어야함 파일 이름이 영화의 id.
    # 개봉일 정보 (release_date), 그중 월을 뽑아내서 12월인가 확인해서 맞으면 title 리스트에 추가
    title = []  
    for i in movies:
        j = i['id']
        movie_file_json = open(f'data/movies/{j}.json',mode = 'r',encoding="UTF-8")
        movie_file_list = json.load(movie_file_json)
        release_date = movie_file_list['release_date']
        if int(release_date[5:7]) == 12:
            title.append(movie_file_list['title'])

    return title
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
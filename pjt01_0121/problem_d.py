import json


def max_revenue(movies):
    
    # 여기에 코드를 작성합니다.  
    
    # 각각의 수익의 비교하여 가장 큰 수익을 가진 영화 title 출력
      # 각각의 수익을 리스트로 묶기
       # 각각의 파일을 열어야함 파일 이름이 영화의 id.
    a = []   
    for i in movies:
        j = i['id']
        movie_file_json = open(f'data/movies/{j}.json',mode = 'r',encoding="UTF-8")
        movie_file_list = json.load(movie_file_json)
        revenue = movie_file_list['revenue']
        a.append(revenue)
        
    # 수익 리스트 a중 가장 큰 값 찾아 index로 위치 알기
    def big(x):
        result = x[0]
        for i in x:
            if result < i:
                result = i
        return x.index(result)
    
    big(a)

    # movies 리스트[big(a)]의 영화의 제목 출력
    title = movies[big(a)]['title']
    
    return title


 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))

    
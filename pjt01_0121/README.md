# 2022년 1월 21일 1차 관통프로젝트

반드시 활용하였던 데이터 정보 정리 및 저장한 파일에 대한 설명과 학습 내용을 README.md 에 기록하여 제출합니다. 

### 1. 데이터 설명

1. genres.json

   * genres.json은 장르의 id, name 정보를 가지고 있습니다.

   * 활용 : problem_b.py, problem_c.py

   

2. movie.json

   * movie.json은 ‘쇼생크 탈출’ 영화 정보를 가지고 있습니다.

   * 활용 : problem_a.py, problem_b.py

   

3. movies.json

   * movies.json은 영화 전체 정보를 가지고 있습니다.

   * 활용 : problem_c.py, problem_d.py, problem_e.py

   

4. movies 폴더 안 22개 json 파일

   * movies 폴더 내부의 파일들은 각 영화의 상세정보를 가지고 있습니다.

   * 활용 : problem_d.py, problem_e.py



### 2. .py 파일 설명

공통 :  

​	주어진 데이터(1,2,3)를 JSON으로 변환 후 객체로 변환해서 사용



1. problem_a.py

   *  문제 : 제공되는 영화 데이터의 주요내용 수집 

     샘플 영화 데이터 중 서비스 구성에 필요한 정보만 반환하는 함수 완성하기

   * 주어진 데이터 

     데이터 2

   * 코드 설명

     * movie_dict 딕셔너리에(주어진 영화데이터)에서 lst(필요한 정보) 에 있는 key에 맞는 value 값을 dict_movie 딕셔너리에 추가

     * dict_movie (서비스 구성에 필요한 정보) 반환

       

2. problem_b.py

   * 문제 : 제공되는 영화 데이터의 주요내용 수정 

     problem_a.py 에서 만들었던 데이터 중 genre_ids를 데이터 1을 활용하여 genre_names로 바꿔 반환하는 함수를 완성하기

   * 주어진 데이터

     데이터 1, 데이터 2

   * 코드 설명

     * movie_dict 딕셔너리에(주어진 영화데이터)에서 lst(필요한 정보) 에 있는 key에 맞는 value 값을 dict_movie 딕셔너리에 추가
     * genre_ids값과 genres의 id 값이 같다면 genres의 name 값을 genre_names 리스트에 추가
     * genre_names를 dict_movie 에 추가
     * dict_movie (서비스 구성에 필요한 정보) 반환

   

3. problem_c.py

   * 문제 : 다중 데이터 분석 및 수정

     데이터 3의 genre_id 부분을 데이터 1을 활용하여 genre_names로 바꾸어 반환하는 함수 완성하기

   * 주어진 데이터

     데이터 1, 데이터 3

   * 코드 설명

     * 필요 정보(lst) key에 맞는 value를 딕셔너리에 추가해서 딕셔너리를 리스트로 합친다.
     * genre_ids값과 genres의 id 값이 같다면 genresd의 name 값을 genre_names 리스트에 추가
     * genre_names를 dict_movie 에 추가
     * lst_movies (모든 영화의 서비스 구성에 필요한 정보) 반환

4. problem_d.py

   * 문제 : 알고리즘을 통한 데이터 출력

     모든 영화의 수익을 비교하여 가장 큰 수익을 가진 영화 title 출력

   * 주어진 데이터

     데이터 3, 데이터 4

   * 코드 설명

     * 데이터 4에 있는 JSON 파일들을 for문을 사용해 객체로 불러들여 세부사항에서 revenue(수익)을 각각 추출해서 리스트(a)로 묶음
     * 수익 리스트(a) 의 요소 중 가장 큰 값의 해당하는 인덱스를 활용하여 해당 영화 제목을 출력

   

5. problem_e.py

   * 문제 : 알고리즘을 통한 데이터 출력

     모든 영화의 개봉월이 12월인 영화들의 title를 리스트로 출력

   * 주어진 데이터

     데이터 3, 데이터 4

   * 코드 설명

     * 데이터 4에 있는 JSON 파일들을 for문을 사용해 객체로 불려들여 세부사항에서 release_date(개봉일)을 각각 추출해 월에 해당하는 부분이 12인지 확인
     * 개봉월이 12월에 해당하는 파일 객체의 title을 리스트 title에 추가
     * title 반환


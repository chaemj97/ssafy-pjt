# PJT 10

## 구미 2반 임소연

### 의문점

- `vue add router`와 `vue add vuex`를 한번에 해도 괜찮을까?

​	> router/index.js와 store/index.js로 같은 파일 이름이라도 경로가 달라서 괜찮음

- views 파일과 components 파일의 차이?

​	> 딱히 없는 듯. 다만 처리하기 편하게 하나의 파일로 통일하는 게 좋을 듯

- axios는 어떻게 사용해야 하나?

​	> 0510_workshop에서 유튜브 API 사용했던 것처럼 처리하자



### router 

- path 설정 ('/', '/random', '/watch-list')
- App.vue에서 `<router-link to="/...">...</router-link>`사용해서 링크 걸기



### vuex

- state에 movies 배열, lists 배열 저장
- HomeView를 접속하는 순간 TMDB API에서 인기 20개의 영화를 불러와서 저장
- WatchListForm에 입력받은 값을 lists에 추가해서 저장



### Home

- movies 로드
  - HomeView created()
  - store actions load_movies(context)
    - params에 api_key, language, region 설정
    - axios로 TMDB API에 get 요청, response.data.results를 commit()
  - store mutations LOAD_MOVIES(state, movielist) 에서 state.movie에 movielist 저장

영화정보를 HomeView, RandomView에 사용



### Random



### WatchList

- Todo앱 했던 것처럼



### bootstrap으로 마지막에 꾸미기



## 구미 2반 채민지

vue와 vuex를 각각 썼을 때보다 합쳐서 쓰니 헷갈려서 어려웠습니다.  아직 둘 다 익숙하지 않아 코드를 적는데 어려움이 있었습니다. 조금씩 구현할 수록 무언가 완성되어 가고 있어 뿌듯했습니다. 관통프로젝트를 시작하기 전보다 완성 후에 조금 더 vuex/vue에 익숙해졌습니다. 개념 부분에 헷갈리는 부분이 많아 다음주 수업을 위해 이번 주말동안 vuex를 제대로 공부해야겠다고 생각했습니다.


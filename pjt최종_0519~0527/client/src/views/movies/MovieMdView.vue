<template>
  <div class="container container2">
    <h1>{{month}}월 {{getWeekNo(new Date())}}째주 MD PICK</h1>
    <br>
    <hr>
    <div class="d-flex justify-content-center">
      <div class="con first container row p-3 m-0 w-75 ">
        <div class="col-3">
          <div class="row">
            <div class="col-12">
              <img id='img' src="../../assets/im.png" alt="캐릭터" width="100%">
            </div>
            <div class="col-12">
              <br>
              
              <h3>빛창목</h3><br>
              <span>
                잔잔한 사람 사는 이야기 영화를 좋아해! 시리즈물은 이전 편을 보지 않은 경우는 선호하지 않아.
                피 튀기는 장면을 싫어하지만 무서운 건 잘 보는 편!! SF영화를 특히 좋아해
              </span>
            </div>
          </div>
        </div>
        

        <b-card-group class="d-flex justify-content-center col-9 p-0">
          <div v-for="movie in md.first" :key="movie.pk">
            <router-link :to="{name: 'movie', params: {moviePk: movie.pk}}">
              <div class="hover m-3">
                <figure>
                  <b-card overlay
                    :img-src="'https://image.tmdb.org/t/p/w500'+movie.poster_path"
                    >
                  </b-card>
                </figure>
              </div>
            </router-link>
          </div>
        </b-card-group>

        
      </div>
    </div>
    <br>
    <br>
    <div class="d-flex justify-content-center">
      <div class="con second container row p-3 m-0 w-75 ">
        <div class="col-3">
          <div class="row">
            <div class="col-12">
              <br>
              <img id='img' src="../../assets/so.png" alt="캐릭터" width="100%">
            </div>
            <div class="col-12">
              <br>
              <h3>소소</h3>
              <br>
              <p>영화든 드라마든 시작하면 끝을 보는 타입. 그래서 작품 선택하기까지 시간이 오래걸려. 실패하지 않는 선택을 위해 보장된 재미를 우선시해. 코미디 장르를 좋아하고 약간의 액션이 들어가면 금상첨화!</p>
            </div>
          </div>
        </div>
        

        <b-card-group class="d-flex justify-content-center col-9 p-0">
          <div v-for="movie in md.second" :key="movie.pk">
            <router-link :to="{name: 'movie', params: {moviePk: movie.pk}}">
              <div class="hover m-3">
                <figure>
                  <b-card overlay
                    :img-src="'https://image.tmdb.org/t/p/w500'+movie.poster_path"
                    >
                  </b-card>
                </figure>
              </div>
            </router-link>
          </div>
        </b-card-group>

        
      </div>
    </div>
    <br>
    <br>
    <div class="d-flex justify-content-center">
      <div class="con first container row p-3 m-0 w-75 ">
        <div class="col-3">
          <div class="row">
            <div class="col-12">
              <br>
              <img id='img' src="../../assets/minji.png" alt="캐릭터" width="100%">
            </div>
            <div class="col-12">
              <br>
              <h3>챔쓰</h3>
              <br>
              <p>
                안녕? 난 영화는 엄청 웃기거나 슬퍼서 눈물 나는 한국 영화를 좋아해! 
                또 잘생긴 배우 나오면 또 챙겨보는 편이야 ㅎㅎ 
                소리가 엄청 큰 영화(액션, 공포, 스릴러)는 좋아하지 않아..
              </p>
            </div>
          </div>
        </div>
        

        <b-card-group class="d-flex justify-content-center col-9 p-0">
          <div v-for="movie in md.third" :key="movie.pk">
            <router-link :to="{name: 'movie', params: {moviePk: movie.pk}}">
              <div class="hover m-3">
                <figure>
                  <b-card overlay
                    :img-src="'https://image.tmdb.org/t/p/w500'+movie.poster_path"
                    >
                  </b-card>
                </figure>
              </div>
            </router-link>
          </div>
        </b-card-group>

        
      </div>
    </div>


    <br><br><br>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'

export default {
  name: 'MovieMd',
  data(){
    return{
      month:'',
    }
  },
  computed: {
    ...mapGetters(['time','md']),
    poster_path: function() {
      return 'https://image.tmdb.org/t/p/w500/'
    }
  },
  methods:{
    ...mapActions(['fetchMovieTime','fetchMovieMd']),
    nowTime() {
      let mm = new Date().getMonth()+1
      this.month = `${mm}`
    },
    getWeekNo(v_date_str) {
      var date = new Date();
      if(v_date_str){
        date = new Date(v_date_str);
      }
      return Math.ceil(date.getDate() / 7);
    }
  },
  created() {
    this.nowTime()
    setInterval(this.nowTime.bind(this), 1000)
    this.fetchMovieTime()
    this.fetchMovieMd()
  }
}
</script>

<style>
.card-img {
  height: 15rem;
  width: 10rem;
  object-fit: cover;
}
#img{
  width: 100%;
}
.con {
  border: 1px solid rgb(200, 192, 192);
}
.a {
  display: flex;
  justify-content: space-between;
  margin: 0 70px;
  margin-top: 65px;
  flex-wrap: wrap;
        /* float: left; */
}
</style>
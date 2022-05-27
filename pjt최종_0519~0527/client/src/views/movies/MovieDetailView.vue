<template>
  <div class="container w-75 container2">
    <h1>MOVIE-DETAIL</h1>
    <br><hr><br>
    <div class="d-flex justify-content-center">
      <div class="w-75 p-4 bg-dark text-white">
        <b-container >
          <b-row>
            <b-col cols="4">
              <img :src="'https://image.tmdb.org/t/p/w500/'+movie.poster_path">
            </b-col>
            <b-col cols="8" style="text-align:left;">
              <h1 style="display:inline;">{{movie.title}}</h1>
              <h3 style="display:inline; vertical-align: top;">
                <span class="mx-3 badge" style="background-color:#26A69A">{{movie.vote_average}}</span>
              </h3>
              <h3 class="text-danger" v-if="isLoggedIn" style="display:inline; vertical-align: top;">
                <i v-if="!isLiked" class="h3 bi bi-bookmark-heart" @click="likeMovie(moviePk); Liked();"></i>
                <i v-if="isLiked" class="h3 bi bi-bookmark-heart-fill" @click="likeMovie(moviePk); Liked();"></i>
                {{likeCount}}
              </h3>
              <p>
                <span class="m-1 badge rounded-pill text-black" style="background-color:#A9D9D0" v-for="genre in movie.genres" :key="genre.id">
                  {{genre.name}} 
                </span>
              </p>
              <p>
                {{movie.overview}}
              </p>
              <p>
                개봉일 : {{movie.release_date}}
              </p>
            </b-col>
          </b-row>
        </b-container>
      </div>
    </div>
    
    
    <!-- Review -->
    <div class="d-flex justify-content-center"> 
      <div class="p-5 w-75">
        <hr>
        <movie-review-list :reviews="movie.review_set"></movie-review-list>
      </div>
    </div>   

    <!-- 뒤로 가기 버튼 -->
    <div id="holder" class="d-flex justify-content-center">
      <div class="button" @click="back">
          <p class="btnText">BACK</p>
          <div class="btnTwo">
            <p class="btnText2">X</p>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import MovieReviewList from '@/components/MovieReviewList.vue'

export default {
  name: 'MovieDetail',
  components: {
    MovieReviewList
  },
  data() {
    return {
      isLiked: false,
      moviePk: this.$route.params.moviePk,
    }
  },
  computed: {
    ...mapGetters(['movie', 'isLoggedIn', 'currentUser']),
    likeCount() {
      return this.movie.like_users?.length
    },
  },
  methods: {
    ...mapActions(['fetchMovie', 'likeMovie', ]),
    back(){
        this.$router.back()
    },
    Liked() {
      this.isLiked = !this.isLiked
    }
  },
  created() {
    this.fetchMovie(this.moviePk)
  },
}
</script>

<style>
.col-4 img{
  width: 100%;
}

</style>
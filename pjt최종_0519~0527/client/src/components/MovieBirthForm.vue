<template>
  <div>
    <div>
      <input type="date" v-model="birthday" required>
      <button class="btn btn-sm sz2 m-2" @click="onSubmit" id="b">MY-BIRTHDAY</button>
    </div>
    <br>
    <img v-if="bi" src="https://i.pinimg.com/originals/fd/2c/1a/fd2c1a96b654e220d09525f006482477.gif" alt="" width="600">
    <div v-if="birthmovie" class="d-flex justify-content-center" >
      <b-card-group v-if="isBirth" class="col-9 p-0 d-flex justify-content-center">
        <movie-birth-list 
        v-for="b in birth"
        :key="b.title"
        :b="b"></movie-birth-list>
      </b-card-group>
      <div v-if="!isBirth">
        <h1>꽝!</h1>
        <h3>대신 이 영화를 추천합니다</h3>
        <div>
          <b-card-group class="p-0 d-flex justify-content-center">
            <router-link :to="{name: 'movie', params: {moviePk: 598}}">
              <div class="hover m-3">
                <figure>
                  <b-card overlay
                    img-src="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/jnSPRyaBnjWGVqeBNyLCl8rAj1d.jpg">
                  </b-card>
                </figure>
              </div>
            </router-link>
          </b-card-group>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieBirthList from "@/components/MovieBirthList.vue"
import {mapGetters} from 'vuex'

export default {
  name : "MovieBirthForm",
  components :{ 
    MovieBirthList
  },
  computed: {
    ...mapGetters(['birth']),
    isBirth() {
      console.log(this.birth?.length)
      if (this.birth?.length === 0) {
        return false
      } else {
        return true
      }
    }
  },
  data() {
    return {
      birthday: '',
      bi: '',
      birthmovie:'',
      none:''
    }
  },
  methods: {
    onSubmit() {
      this.birthmovie = false
      this.bi = true
      setTimeout(function(){
        this.$store.dispatch('searchMovie',{ birthday: this.birthday})
        this.bi= false
        this.birthmovie = true
        }.bind(this),4000)
    },
  },
}
</script>

<style>
.card-img {
  height: 20rem;
  width: 15rem;
  object-fit: cover;
}
</style>
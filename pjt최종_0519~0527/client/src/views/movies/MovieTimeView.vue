<template>
  <div class="container container2">
    <h1>지금 이 순간!</h1>
    <br>
    <hr>
    <div class="clock">
      <h1><i class="bi bi-alarm"></i>  {{now}}</h1>
      <br>
    </div>
    <div v-for="(value, key) in time" :key="key">
      <h2>{{key}}</h2>
      <br>
      <carousel-3d :controls-visible="true" :clickable="true" :width="200" :height="250" :display="9">
        <slide v-for="(t, i) in time[key]" :index="i" :key="t.pk">
          <figure>
            <img :src="'https://image.tmdb.org/t/p/w500'+t.poster_path">
            <figcaption>
              <router-link :to="{name: 'movie', params: {moviePk: t.pk}}">
                {{t.title}}
              </router-link>
            </figcaption>
          </figure>
        </slide>
      </carousel-3d>
      <br>
    </div>
    <hr><br>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'

export default {
  name: 'MovieTime',
  data() {
    return {
      now: 0,
    }
  },
  computed: {
    ...mapGetters(['time'])
  },
  methods: {
    ...mapActions(['fetchMovieTime']),
    nowTime() {
      let hh = new Date().getHours() < 10 ? "0"+new Date().getHours() : new Date().getHours()
      let mm = new Date().getMinutes() < 10 ? "0"+new Date().getMinutes() : new Date().getMinutes()
      let ss = new Date().getSeconds() < 10 ? "0"+new Date().getSeconds() : new Date().getSeconds()
      this.now = `${hh}:${mm}:${ss}`
    }
  },
  created() {
    this.nowTime()
    setInterval(this.nowTime.bind(this), 1000)
    this.fetchMovieTime()
  }
}

</script>

<style>
a {
  color: black;
  text-decoration: none;
}

.card-img {
  height: 15rem;
  object-fit: cover;
}
</style>
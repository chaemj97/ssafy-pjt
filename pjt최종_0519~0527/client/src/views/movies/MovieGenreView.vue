<template>
  <div class="container container2">
    <h1>장르별 추천</h1>
    <br>
    <div v-for="(value, key) in genres" :key="key">
      <hr>
      <h2>{{key}}</h2>
      <br>
      <carousel-3d :controls-visible="true" :clickable="true" :width="200" :height="250" :display="9">
        <slide v-for="(genre, i) in genres[key]" :index="i" :key="genre.pk">
          <figure>
            <img :src="'https://image.tmdb.org/t/p/w500'+genre.poster_path">
            <figcaption>
              <router-link :to="{name: 'movie', params: {moviePk: genre.pk}}">
                {{genre.title}}
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
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'MovieGenre',
  computed: {
    ...mapGetters(['genres'])
  },
  methods: {
    ...mapActions(['fetchMovieGenre'])
  },
  created() {
    this.fetchMovieGenre()
  },
}
</script>

<style>


figcaption a {
  color: white;
  text-decoration: none;
}

.carousel-3d-container figure {
  margin:0;
}

.carousel-3d-container figcaption {
  position: absolute;
  background-color: rgba(0, 0, 0, 0.5);
  color: #fff;
  bottom: 0;
  position: absolute;
  bottom: 0;
  padding: 15px;
  font-size: 12px;
  min-width: 100%;
  box-sizing: border-box;
}

.card-img {
  height: 15rem;
  object-fit: cover;
}
</style>
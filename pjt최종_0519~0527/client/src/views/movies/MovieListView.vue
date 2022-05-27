<template>
  <div class="container container2">
    <h1>SSA-NEMA</h1>
    <br>
    <hr>
    
    <carousel-3d :autoplay="true" :autoplay-timeout="4000" :controls-visible="true" :clickable="true" :width="200" :height="250" :display="9">
      <slide v-for="(movie, i) in topten" :index="i" :key="movie.pk">
        <figure>
          <img :src="'https://image.tmdb.org/t/p/w500'+movie.poster_path">
          <figcaption>
            <router-link :to="{name: 'movie', params: {moviePk: movie.pk}}">
              {{movie.title}}
            </router-link>
          </figcaption>
        </figure>
      </slide>
    </carousel-3d>
    <hr>
    <br>
    <h1>TODAY-RANDOM</h1>
    <br>
    <b-card-group class="d-flex justify-content-center">
      <div v-for="movie in movies" :key="movie.pk">
        <router-link :to="{name: 'movie', params: {moviePk: movie.pk}}">
          <div class="hover m-3">
            <figure>
              <b-card overlay
                :img-src="'https://image.tmdb.org/t/p/w500'+movie.poster_path"
                style="max-width: 10rem;">
              </b-card>
            </figure>
          </div>
        </router-link>
      </div>
    </b-card-group>
    <br><br>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'MovieList',
  data() {
    return {
      slide: 0,
      sliding: null
    }
  },
  computed: {
    ...mapGetters(['movies', 'topten']),
  },
  methods: {
    ...mapActions(['fetchMovies', 'fetchTopTen']),
    onSlideStart() {
      this.sliding = true
    },
    onSlideEnd() {
      this.sliding = false
    }
  },
  created() {
    this.fetchTopTen()
    this.fetchMovies()
  },
}
</script>

<style>
a {
  color: black;
  text-decoration: none;
}

figure div .card-img {
  height: 15rem;
  object-fit: cover;
}

figure {
	margin: 0;
	padding: 0;
	background: #fff;
	overflow: hidden;
}

.hover figure img {
	opacity: 1;
	-webkit-transition: .3s ease-in-out;
	transition: .3s ease-in-out;
}
.hover figure:hover img {
	opacity: .5;
}

</style>
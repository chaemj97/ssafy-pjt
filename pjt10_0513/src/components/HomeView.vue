<template>
  <div class="container">
    <div class="home row">
      <movie-card
        v-for="movie in movies"
        :key="movie.title"
        :movie="movie"
        class="col"></movie-card>
    </div>
  </div>

</template>

<script>
import MovieCard from '@/components/MovieCard.vue'


export default {
  name: 'HomeView',
  components: {
    MovieCard
  },
  computed: {
    movies: function() {
      return this.$store.state.movies
    }
  },
  created() {
    this.$store.dispatch('load_movies')
  }
}
</script>

<template>
  <div class="home">
    <movie-card
      v-for="movie in movies"
      :key="movie.title"
      :movie="movie"></movie-card>
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

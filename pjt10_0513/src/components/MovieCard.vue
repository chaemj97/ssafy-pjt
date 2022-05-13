<template>
  <div>
    <div class="card" style="width: 18rem;">
      <img :src="poster_path" class="card-img-top" alt="cardimg">
      <div class="card-body">
        <h5 class="card-title">{{title}}</h5>
        <p class="card-text">{{overview}}</p>
      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'MovieCard',
  props: {
    movie: Object,
  },
  computed: {
    title: function() {
      return this.movie.title
    },
    overview: function() {
      return this.movie.overview
    },
    poster_path: function() {
      return 'https://image.tmdb.org/t/p/w500'+this.movie.poster_path
    }
  }
}
</script>

<style>

</style>
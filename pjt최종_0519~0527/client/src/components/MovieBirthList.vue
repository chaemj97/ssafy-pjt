<template>
  <div>
    <router-link :to="{name: 'movie', params: {moviePk: b.pk}}">
      <div class="hover m-3">
        <figure>
          <b-card overlay
            :img-src="poster_path">
          </b-card>
        </figure>
      </div>
    </router-link>
  </div>
  
</template>

<script>

export default {
  name : "MovieBirthList",
  props: { b: Object },
  computed: {
    poster_path: function() {
      return 'https://image.tmdb.org/t/p/w500'+this.b.poster_path
    }
  }
  
}
</script>

<style>
.card-img {
  height: 20rem;
  width: 15rem;
  object-fit: cover;
}
</style>
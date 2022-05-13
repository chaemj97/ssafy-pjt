<template>
  <div class="random">
    <button @click="randomMovie" >PICK</button>
    <div class="card" style="width: 18rem;">
      <img :src="poster_path" class="card-img-top" alt="Pick a MOVIE">
      <div class="card-body">
        <h5 class="card-title">{{title}}</h5>
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  
  name: 'RandomView',
  data : function() {
    return {
      title: '',
      poster_path: '',
    }
  },
  methods : {
    randomMovie : function(){
      const index = _.sample(_.range(0,20))
      const rm = this.$store.state.movies[index]
      this.title = rm.title
      this.poster_path = 'https://image.tmdb.org/t/p/w500' + rm.poster_path
    }
  },    
  
}
</script>
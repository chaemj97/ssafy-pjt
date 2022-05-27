<template>
  <div class="container container2">
    <h1>나의 생일에 개봉한 영화 <i class="bi bi-emoji-smile"></i></h1>
    <br>
    <hr>
    <movie-birth-form></movie-birth-form>
    <br>
    
    
  </div>
</template>

<script>
import MovieBirthForm from "@/components/MovieBirthForm.vue"

export default {
  name: "movieBirth",
  components :{ 
    MovieBirthForm
  },
  
}
</script>

<style>

</style>
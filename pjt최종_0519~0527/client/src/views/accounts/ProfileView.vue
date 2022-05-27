<template>
  <div class="container container2">
    <h1>'{{profile.username}}' PROFILE</h1>
    <br><hr>
    <div>
      <br>
      <h3>찜한 영화</h3>
      <br>
      <div class="d-flex justify-content-center" >
        <b-card-group class="d-flex justify-content-center col-9 p-0">
          <div v-for="movie in profile.like_movies" :key="movie.pk">
            <router-link :to="{name: 'movie', params: {moviePk: movie.pk}}">
              <div class="hover m-3">
                <figure>
                  <b-card overlay
                    :img-src="'https://image.tmdb.org/t/p/w500'+movie.poster_path"
                    >
                  </b-card>
                </figure>
              </div>
            </router-link>
          </div>
        </b-card-group>
      </div>
      <br>
      
    </div>
    
    

    <div class="container w-75">
      <hr>
      <br>
      <h3>작성한 게시글</h3>
      <br>
      <div class="d-flex justify-content-center">
        <table class="w-75 table table-striped table-hover">
          <colgroup>
            <col width="300px"/>
            <col width="600px"/>
          </colgroup>
          <tbody>
            <tr v-for="article in profile.article_set" :key="article.pk">
              <th>no.{{article.pk}} : </th>
              <td><span id='title' @click="title(article)">{{article.title}}</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <br>

    <div class="container w-75">
      <hr>
      <br>
      <h3>좋아요 한 게시글</h3>
      <br>
      <div class="d-flex justify-content-center">
        <table class="w-75 table table-striped table-hover">
          <colgroup>
            <col width="300px"/>
            <col width="600px"/>
          </colgroup>
          <tbody>
            <tr v-for="article in profile.like_articles" :key="article.pk">
              <th>no.{{article.pk}} : </th>
              <td><span id='title' @click="title(article)">{{article.title}}</span></td>
            </tr>
          </tbody>
        </table>
      </div>

    </div>
    <br><br>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ProfileView',
  methods: {
    ...mapActions(['fetchProfile']),
    title(article){
        this.$router.push({name: 'article', params: {articlePk: article.pk}})
      }
  },
  computed: {
    ...mapGetters(['profile'])
  },
  created() {
    const payload = {username: this.$route.params.username}
    this.fetchProfile(payload)
  }
}
</script>

<style>
#title{
    cursor : pointer;
    text-align:left;
  }
</style>
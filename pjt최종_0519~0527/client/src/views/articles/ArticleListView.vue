<template>
  <div class="container container2">
    <h1>COMMUNITY</h1>
    <br>
    <hr>
    
    <table class="table table-hover">
      <colgroup>
        <col width="300px"/>
        <col width="900px"/>
        <col width="300px"/>
        <col width="300px"/>
      </colgroup>
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col" id="title">Title</th>
          <th scope="col">User</th>
          <th scope="col">CREATE_TIME</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="article in articles" :key="article.pk">
          <th scope="row">{{article.pk}}</th>
          <td id="title">
            <p @click="title(article)">{{article.title}}</p>
          </td>
          <td>{{ article.user.username }}</td>
          <td>{{ article.created_at.substr(0,10) }}</td>
        </tr>          
      </tbody>
    </table>
    
    <br>
    <div id="holder" class="d-flex justify-content-center">
      <div class="button" @click="articleCreate">
          <p class="btnText">NEW CREATE?</p>
          <div class="btnTwo">
            <p class="btnText2">GO!</p>
          </div>
      </div>
    </div> 
    <br><br><br>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'ArticleList',
    computed: {
      ...mapGetters(['articles']),
    },
    methods: {
      ...mapActions(['fetchArticles']),
      articleCreate(){
        this.$router.push({ name: 'articleNew' })
      },
      title(article){
        this.$router.push({name: 'article', params: {articlePk: article.pk}})
      }
    },
    created() {
      this.fetchArticles()
    },
  }
</script>

<style>
  #title{
    text-align:left;
    cursor : pointer;

  }
  .button {
  background: #3D4C53;
  margin : auto;
  width : 200px;
  height : 50px;
  overflow: hidden;
  text-align : center;
  transition : .2s;
  cursor : pointer;
  border-radius: 3px;
  box-shadow: 0px 1px 2px rgba(0,0,0,.2);
  }
  .btnTwo {
    position : relative;
    width : 200px;
    height : 150px;
    margin-top: -100px;
    padding-top: 2px;
    background : #26A69A;
    left : -250px;
    transition : .3s;
  }
  .btnText {
    color : white;
    transition : .3s;
    margin-top : 13px;
    margin-bottom : 13px;
  }
  .btnText2 {
    margin-top : 60px;
    margin-right : -130px;
    color : #FFF;
  }
  .button:hover .btnTwo{ /*When hovering over .button change .btnTwo*/
    left: -130px;
  }
  .button:hover .btnText{ /*When hovering over .button change .btnText*/
    margin-left : 65px;
  }
  .button:active { /*Clicked and held*/
    box-shadow: 0px 5px 6px rgba(0,0,0,0.3);
  }
</style>

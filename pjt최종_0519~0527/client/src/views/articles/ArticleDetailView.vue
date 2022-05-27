<template>
  <div class="container container2 w-75">
    <hr>
    <div class="container w-75">
      

      <h1 class="fw-bold d-flex justify-content-start">{{ article.title }}</h1>
      <p class="text-secondary d-flex justify-content-start">{{article.user.username}} {{ article.created_at.substr(0,10) }}</p> 
      
      <hr>
      <p class=" d-flex justify-content-start">
        {{ article.content }}
      </p>
      <hr>
      <!-- 자기가 쓴 글에만 -->
      <div v-if="isAuthor" class="tar">
        <button class="btn btn-sm sz2 m-2 float-right" @click="edit" id="b">EDIT?</button>
        <button class="btn btn-sm sz2 m-2" @click="deleteArticle(articlePk)" id="b">DELETE</button>
      </div>
      <!-- 자기가 쓴 글이 아니면 -->
      <div v-if="!isAuthor">
        <p class="d-flex justify-content-end" @click="likeArticle(articlePk)" id="good">
          <i class="bi bi-hand-thumbs-up-fill"></i> 좋아요 {{ likeCount }}
        </p>
      </div>
      
      <p class="fw-bold d-flex justify-content-start">총 <span class="text-primary">{{commentCount}}</span>건의 댓글이 있습니다.</p>
      
      <hr />
      <!-- Comment UI -->
      
      <comment-list :comments="article.comment_set"></comment-list>

      <div id="holder" class="d-flex justify-content-center">
        <div class="button" @click="back">
          <p class="btnText">BACK</p>
          <div class="btnTwo">
            <p class="btnText2">X</p>
          </div>
        </div>
      </div>
    </div>
    <br><br><br>
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/CommentList.vue'

  export default {
    name: 'ArticleDetail',
    components: { CommentList },
    data() {
      return {
        articlePk: this.$route.params.articlePk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article']),
      likeCount() {
        return this.article.like_users?.length
      },
      commentCount(){
        return this.article.comment_set?.length
      }
    },
    methods: {
      ...mapActions([
        'fetchArticle',
        'likeArticle',
        'deleteArticle',
      ]),
      back(){
        this.$router.push({name:'articles'})
      },
      edit(){
        this.$router.push({ name: 'articleEdit', params: this.articlePk })
      }
    },
    created() {
      this.fetchArticle(this.articlePk)
    },
  }
</script>

<style>
  #b{
    background : #3D4C53;
    color: white;
    padding-right: 15px;
    padding-left: 15px;
  
  }
  .tar {
    text-align: right;
  }
  /* 글 */
  #holer{
    text-align: right;
  }
  #good {
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

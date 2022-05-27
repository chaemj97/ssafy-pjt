<template>
  <form @submit.prevent="onSubmit" >
    <div class="container article-form w-75">
      <div class="d-flex justify-content-center w-100 m-0" >
        <br>
        <label for="ti" class="fs-3 me-2">TITLE :</label>
        <textarea v-model="newArticle.title" type="text" id="ti" rows="1" cols="80"></textarea>
      </div>
      <hr>
      <div class="d-flex justify-content-center w-100" >
        <label for="content" class="fs-3 me-2">CONTENT :</label>
        <textarea v-model="newArticle.content" type="text" id="content" rows="10" cols="80"></textarea>
        <br>
      </div>
    </div>
    <br>
    <div>
      <div id="holder" class="d-flex justify-content-center">
        <div class="button" @click="onSubmit">
            <p class="btnText">{{action}}</p>
            <div class="btnTwo">
              <p class="btnText2">GO!</p>
            </div>
        </div>

        <div class="button" @click="back">
            <p class="btnText">CANCEL</p>
            <div class="btnTwo">
              <p class="btnText2">X</p>
            </div>
        </div>
      </div>
    </div>
  </form>
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'ArticleForm',
    props: {
      article: Object,
      action: String,
    },
    data() {
      return {
        newArticle: {
          title: this.article.title,
          content: this.article.content,
        }
      }
    },

    methods: {
      ...mapActions(['createArticle', 'updateArticle']),
      onSubmit() {
        if (this.action === 'CREATE?') {
          this.createArticle(this.newArticle)
        } else if (this.action === 'UPDATE?') {
          const payload = {
            pk: this.article.id,
            ...this.newArticle,
          }
          this.updateArticle(payload)
        }
      },
      back(){
        this.$router.back()
      }
    },
  }
</script>

<style>
.article-form {
  border: 2px solid black;
  padding: 20px;
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

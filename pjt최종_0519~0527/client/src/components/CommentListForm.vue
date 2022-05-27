<template>
  <div>
    <div class="reply-write-area">
      <div class="rw-inner">
        <div class="textarea">
          <textarea class="form-control noresize" placeholder="댓글을 입력하세요." id="answerCont" maxlength="4000" v-model="content" required></textarea>
        </div>
        <div class="btns tar">
          <button class="btn btn-sm sz2 m-2" @click="onSubmit" id="b">SUBMIT</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['article']),
  },
  methods: {
    ...mapActions(['createComment']),
    onSubmit() {
      this.createComment({ articlePk: this.article.id, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style>
/* 댓글 */
  
  .reply-write-area {
    padding-top: 15px;
    padding-right: 15px;
    padding-left: 15px;
    background: #fafbfc;
    border: 1px solid #e3e7eb;
  }
  .tar {
    text-align: right;
  }
</style>
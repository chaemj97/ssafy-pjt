<template>
  <div class="comment-list">
    <comment-list-form></comment-list-form>
  <table class="table">
    <tbody>
      <tr>
        <comment-list-item 
        v-for="comment in comments"
        :key="comment.content"
        :comment="comment">
        </comment-list-item> 
      </tr>
    </tbody>
  </table>

  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem.vue'
import CommentListForm from '@/components/CommentListForm.vue'


export default {
  name: 'CommentList',
  components: { 
    CommentListForm, 
    CommentListItem
    },
  props: { 
    comments: Array
    },
}
</script>

<style>
</style>
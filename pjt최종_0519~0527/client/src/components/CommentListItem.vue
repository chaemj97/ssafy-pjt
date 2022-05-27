<template>
  <div>
    <th scope="row" id="a" @click="profile">
        {{ comment.user.username }}
      </th>
    <td><span v-if="!isEditing">: {{ payload.content }}</span></td>
    <td><span v-if="isEditing">
        <input type="text" v-model="payload.content">
        <button class="btn btn-sm sz2 m-2" id='bb' @click="onUpdate">Update</button> |
        <button class="btn btn-sm sz2 m-2" id='bb' @click="switchIsEditing">Cancle</button>
      </span></td>
    <td><span v-if="currentUser.username === comment.user.username && !isEditing">
        <button class="btn btn-sm sz2 m-2" id='bb' @click="switchIsEditing">Edit</button> |
        <button class="btn btn-sm sz2 m-2" id='bb' @click="deleteComment(payload)">Delete</button>
      </span></td>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListItem',
  props: { comment: Object },
  data() {
    return {
      isEditing: false,
      payload: {
        articlePk: this.comment.article,
        commentPk: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser']),
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    },
    profile(){
      this.$router.push({ name: 'profile', params: { username: this.comment.user.username }})
    }
  },

}
</script>

<style>
  #bb{
    background : #9aa0a4;
    color: white;
    padding-right: 15px;
    padding-left: 15px;
  
  }
  #a {
    cursor : pointer;
  }
</style>
<template>
  <div class="p-3 mb-3 bg-info bg-opacity-50">
    <h1>My Movie List</h1>
    <input
    v-model.trim="ListTitle" type="text">
    <button class="btn btn-primary" @click="createList">Add</button>
  </div>
</template>

<script>
export default {
  name:'WatchListForm',
  data : function() {
    return {
      ListTitle : '',
    }
  },
  methods: {
    createList: function(){
      const newList = {
        title: this.ListTitle,
        id : new Date().getTime()
      }
      this.$store.dispatch('createList', newList)
      this.ListTitle = ''
    }
  }
}
</script>

<style>

</style>
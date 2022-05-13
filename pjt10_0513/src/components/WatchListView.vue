<template>
  <div class="watchlist">
    <watch-list-form></watch-list-form>
    <watch-list-item
    v-for="watchmovie in lists"
    :key='watchmovie.id'
    :watchmovie="watchmovie"></watch-list-item>
  </div>
</template>

<script>
import WatchListForm from '@/components/WatchListForm.vue'
import WatchListItem from '@/components/WatchListItem.vue'
export default {
  name: 'WatchListView',
  components:{
    WatchListForm,
    WatchListItem,
  },
  computed : {
    lists : function(){
      return this.$store.state.lists
    }
  }
}
</script>
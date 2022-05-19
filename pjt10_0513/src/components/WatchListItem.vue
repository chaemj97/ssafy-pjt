<template>
  <div class="p-2 bg-info bg-opacity-10">
    <span>{{watchmovie.title}}</span>
  </div>
</template>

<script>
export default {
  name:'WatchListItem',
  props : {
    watchmovie :Object,
  },
}
</script>

<style>

</style>
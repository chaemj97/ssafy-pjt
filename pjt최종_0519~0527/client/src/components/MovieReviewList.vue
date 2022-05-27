<template>
  <div>
    <ul class="p-0 m-0">
      <h3>Review Rate</h3>
      <movie-review-list-item v-for="review in reviews"
        :key="review.id" :review="review">
      </movie-review-list-item>
    </ul>
    <hr>
    <movie-review-form :reviews="reviews"></movie-review-form>
  </div>
</template>

<script>
import MovieReviewListItem from '@/components/MovieReviewListItem.vue'
import MovieReviewForm from '@/components/MovieReviewForm.vue'

export default {
  name: 'MovieReviewList',
  components: {
    MovieReviewListItem, MovieReviewForm
  },
  props: {
    reviews: Array
  },
}
</script>

<style>

</style>
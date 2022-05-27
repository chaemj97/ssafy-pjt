<template>
  <div v-if="isLoggedIn">
    <div>
      <h3>평점 등록</h3>
      <form @submit.prevent="onSubmit">
        <b-input-group>
          <b-form-rating v-model="score" color="#ff8800" stars="10" size="lg"></b-form-rating>
          <b-input-group-text class="justify-content-center" style="min-width: 3em;">
            {{ score }}
          </b-input-group-text>
          <b-button type="submit">ENROLL</b-button>
        </b-input-group>
      </form>
    </div>
  </div>
  <div v-else>
    <div class="d-grid col-6 mx-auto">
      <router-link :to="{name: 'login'}" class="btn text-white" style="background-color:#26A69A;">평점을 등록하려면 로그인하세요</router-link>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'

export default {
  name: 'MovieReviewForm',
  props: {
    reviews: Array
  },
  data() {
    return {
      score: 0,
      review_user : []
    }
  },
  computed: {
    ...mapGetters(['movie', 'isLoggedIn']),
  },
  methods: {
    ...mapActions(['createReview']),
    onSubmit() {
      this.createReview({moviePk: this.movie.pk, score: this.score,})
      // this.fetchMovie(this.movie.pk)
      this.score = ''
    }
  }
}
</script>

<style>

</style>
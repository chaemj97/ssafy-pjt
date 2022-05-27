<template>
  <div>
    <!-- <div v-if="!isEditing" style="display:inline;">
      <span v-for="score in payload.score" :key="score">
        <i class="m-1 bi bi-star-fill text-warning"></i>
      </span>
    </div> -->
    <div v-if="isLoggedIn">
      <div v-if="isEditing">
        <b-input-group>
          <b-form-rating v-model="payload.score" color="#ff8800" stars="10" size="lg"></b-form-rating>
          <b-input-group-text class="justify-content-center" style="min-width: 3em;">
            {{ payload.score }}
          </b-input-group-text>
          <b-button variant="success" @click="onUpdate">Update</b-button>
          <b-button @click="switchIsEditing">Cancle</b-button>
        </b-input-group>
        <!-- <b-form-rating v-model="payload.score" variant="warning" class="mb-2" stars="10"></b-form-rating>
        <button @click="onUpdate">Update</button>
        <button @click="switchIsEditing">Cancle</button> -->
      </div>
      <div v-if="!isEditing">
        <p v-if="currentUser.username === review.user.username">
          <b-input-group>
            <b-form-rating readonly v-model="payload.score" color="#ff8800" stars="10" size="lg"></b-form-rating>
            <b-input-group-text class="justify-content-center" style="min-width: 3em;">
              {{ payload.score }}
            </b-input-group-text>
            <b-button @click="switchIsEditing">EDIT</b-button>
            <b-button id="delete" @click="deleteReview(payload)">DELETE</b-button>
          </b-input-group>
        </p>
        <p v-else>
          <b-input-group>
            <b-form-rating readonly v-model="payload.score" color="#ff8800" stars="10" size="lg"></b-form-rating>
            <b-input-group-text class="justify-content-center" style="min-width: 3em;">
              {{ payload.score }}
            </b-input-group-text>
            <b-input-group-text class="justify-content-center" style="min-width: 3em;">
              {{ review.user.username }}
            </b-input-group-text>
          </b-input-group>
        </p>
      </div>
    </div>
    <div v-else>
      <router-link :to="{name: 'login'}">
        <button>Login to Rate this Movie</button>
      </router-link>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'

export default {
  name: 'MovieReviewListItem',
  props: {
    review: Object,
  },
  data() {
    return {
      isEditing: false,
      payload: {
        moviePk: this.review.movie.pk, 
        reviewPk: this.review.pk, 
        score: this.review.score,
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser', 'isLoggedIn']),
  },
  methods: {
    ...mapActions(['updateReview', 'deleteReview']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateReview(this.payload)
      // this.fetchMovie(this.review.movie.pk)
      this.isEditing = false
    }
  }
}
</script>

<style>
#delete{
  background-color:#26A69A;
}
</style>
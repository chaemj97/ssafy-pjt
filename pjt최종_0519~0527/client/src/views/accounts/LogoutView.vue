<template>
  <div id="logout" class="container2">
    <div class="border border-3 rounded">
      <h1>Logout</h1>
      <h2>See You Again! <i class="bi bi-emoji-smile"></i></h2>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'LogoutView',
  methods: {
    ...mapActions(['logout'])
  },
  computed: {
    ...mapGetters(['isLoggedIn'])
  },
  created() {
    if (this.isLoggedIn) {
      this.logout()
    } else {
      alert('잘못된 접근입니다.')
      this.$router.back()
    }
  }
}
</script>

<style>
#logout {
  display: flex; justify-content: center; align-items: center;
}
</style>
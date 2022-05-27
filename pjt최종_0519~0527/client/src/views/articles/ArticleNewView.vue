<template>
  <div class="container2">
    <div class="d-flex justify-content-center">
      <div>
        <h1>New Article</h1>
        <hr>
        <article-form :article="article" action="CREATE?"></article-form>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapActions } from 'vuex'
  import ArticleForm from '@/components/ArticleForm.vue'
  export default {
    name: 'AritcleNewView',
    components: { ArticleForm },
    data() {
      return {
        article: {
          pk: null,
          title: '',
          content: '',
        }
      }
    },
    methods: {
      ...mapActions(['fetchCurrentUser'])
    },
    created() {
      this.fetchCurrentUser()
    }
  }
</script>

<style>

</style>

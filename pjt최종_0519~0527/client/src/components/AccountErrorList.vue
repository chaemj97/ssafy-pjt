<template>
  <div>
    <div v-for="(errors, field) in authError" :key="field">
      <ul class="p-0">
        <b-alert show variant="danger" v-for="(error, idx) in errors" :key="idx">
          {{field}} - {{error}}
        </b-alert>
      </ul>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'AccountErrorList',
  computed: {
    ...mapGetters(['authError'])
  }
}
</script>

<style>

</style>
<template>
  <div id="signup" class="container2">
    <div class="border border-3 rounded">
      <h1>Signup</h1>

      <account-error-list v-if="authError"></account-error-list>

      <b-form @submit.prevent="signup(credentials)">
        <b-form-group label="User Name:" label-for="username">
          <b-form-input type="text" id="username" required
            v-model="credentials.username">
          </b-form-input>
        </b-form-group>
        <b-form-group label="Password:" label-for="password1">
          <b-form-input type="password" id="password1" required
            v-model="credentials.password1">
          </b-form-input>
        </b-form-group>
        <b-form-group label="Password Confirm:" label-for="password2">
          <b-form-input type="password" id="password2" required
            v-model="credentials.password2">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" class="mx-2" style="background-color: #26A69A;">SignUp</b-button>
      </b-form>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name: 'SignupView',
  components: {
    AccountErrorList
  },
  data() {
    return {
      credentials: {
        username: '',
        password1: '',
        password2: '',
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['signup'])
  }
}
</script>

<style>
#signup {
  text-align: left;
  display: flex; justify-content: center; align-items: center;
}

#signup a {
  color: white;
  text-decoration:none;
}

#signup div{
  padding: 10px;
}
</style>
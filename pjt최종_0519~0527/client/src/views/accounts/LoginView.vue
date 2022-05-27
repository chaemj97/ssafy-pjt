<template>
  <div id="login" class="container2">
    <div class="border border-3 rounded">
      <h1>Login</h1>
  
      <account-error-list v-if="authError"></account-error-list>
  
      <b-form @submit.prevent="login(credentials)">
        <b-form-group label="User Name:" label-for="username">
          <b-form-input type="text" id="username" required
            v-model="credentials.username">
          </b-form-input>
        </b-form-group>
        <b-form-group label="Password:" label-for="password">
          <b-form-input type="password" id="password" required
            v-model="credentials.password">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" class="mx-2" style="background-color: #26A69A;">LOGIN</b-button>
        <b-button style="background-color: #3D4C53;">
          <router-link :to="{name: 'signup'}">SIGNUP</router-link>
        </b-button>
      </b-form>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import AccountErrorList from '@/components/AccountErrorList.vue'

export default {
  name: 'LoginView',
  components: {
    AccountErrorList
  },
  data: function() {
    return {
      credentials: {
        username: '',
        password: '',
      }
    }
  },
  computed: {
    ...mapGetters(['authError'])
  },
  methods: {
    ...mapActions(['login']),
    
  },
}
</script>

<style>
#login {
  text-align: left;
  display: flex; justify-content: center; align-items: center;
}

#login a {
  color: white;
  text-decoration:none;
}

#login div{
  padding: 10px;
}
</style>
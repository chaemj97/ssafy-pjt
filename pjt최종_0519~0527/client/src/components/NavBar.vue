<template>
  <div>
    <nav id="fix" class="navbar navbar-expand-lg">
      <div class="container-fluid">
        <router-link :to="{name: 'movies'}"><i class="bi bi-film fs-1"> SSA-NEMA</i> </router-link>
        
        <ul class="navbar-nav mb-2 mb-lg-0 d-flex justify-content-end">
          <li class="nav-item" v-if="!isLoggedIn">
            <router-link :to="{name: 'login'}">LOGIN</router-link>
          </li>
          <li class="nav-item" v-if="!isLoggedIn">
            <router-link :to="{name: 'signup'}">SIGNUP</router-link>
          </li>
          <li class="nav-item" v-if="isLoggedIn">
            <router-link :to="{name: 'profile', params: {username}}">
              {{currentUser.username}}
            </router-link>
          </li>
          <li class="nav-item" v-if="isLoggedIn">
            <router-link :to="{name: 'logout'}">LOGOUT</router-link>
          </li>
        </ul>
        
      </div>
    </nav>
    
    <b-navbar id="list" :sticky="true" class="d-flex justify-content-center" >
      <b-navbar-nav>
        <b-nav-item>
          <router-link :to="{name: 'movies'}">MOVIE</router-link>
        </b-nav-item>
        <b-nav-item>
          <router-link :to="{name: 'movieGenre'}">GENRE</router-link>
        </b-nav-item>
        <b-nav-item>
          <router-link :to="{name: 'movieTime'}">TIME</router-link>
        </b-nav-item>
        <b-nav-item>
          <router-link :to="{name: 'movieBirth'}">BIRTHDAY</router-link>
        </b-nav-item>
        <b-nav-item>
          <router-link :to="{name: 'movieMd'}">MD-PICK</router-link>
        </b-nav-item>
        <b-nav-item>
          <router-link :to="{name: 'articles'}">COMMUNITY</router-link>
        </b-nav-item>
      </b-navbar-nav>
      
    </b-navbar>
    
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'NavBar',
  computed: {
    ...mapGetters(['isLoggedIn', 'currentUser']),
    username() {
      return this.currentUser.username ? this.currentUser.username : 'guest'
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
#list{
  background-color:#26A69A;
  font-size: x-large;
}
#fix{
  background-color:#3D4C53;
  font-size: x-large;
  /* margin-bottom:50px; */
}
nav {
  /* padding-top: 45px; */
  padding-bottom: 30px;
  height: 70px;
}

nav a {
  color: white;
  text-decoration: none;
  margin-left: 20px;
  margin-right: 20px;
  padding : 0px
}

#list a.router-link-exact-active {
  /* color: #42b983; */
  color:#3D4C53;
}

#fix a.router-link-exact-active {
  /* color: #42b983; */
  color:#26A69A;
}
</style>
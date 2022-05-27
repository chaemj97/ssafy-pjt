<template>
  <div id="app">
    <nav>
      <nav-bar></nav-bar>
    </nav>
    <router-view></router-view>
    <footer>
      <foot-bar></foot-bar>
    </footer>
    <div style="position: fixed; right: 10px; bottom: 45px;">
      <a href="#">
        <h1><i style="color:#26A69A;" class="bi bi-arrow-up-circle-fill"></i></h1>
      </a>
    </div>
  </div>
</template>

<script>
  import NavBar from '@/components/NavBar.vue'
  import FootBar from '@/components/FootBar.vue'

  export default {
    name: 'App',
    components: {
      NavBar, FootBar
    },
  }
</script>

<style>
#app {
  font-family:'SBAggroL', Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.container2{
  margin-top:100px;
  margin-bottom: 60px;
}
@font-face {
    font-family: 'SBAggroL';
    src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2108@1.1/SBAggroL.woff') format('woff');
    font-weight: normal;
    font-style: normal;
}

</style>

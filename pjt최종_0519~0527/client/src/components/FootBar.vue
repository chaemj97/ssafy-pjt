<template>
  <footer>
    <b-navbar id="fixx" fixed="bottom" class="justify-content-center">
      <h4 class="m-0">© SSAFY 구미 2반 임소연, 채민지</h4>
      <a id="admin" href="http://localhost:8000/admin/">ADMIN</a>
      
    </b-navbar>
  </footer>
</template> 

<script>
export default {
  name: 'FootBar',
}
</script>

<style>
#fixx{
  background-color:#3D4C53;
  color: white;
  height: 50px;
}
#admin{
  color:#3D4C53;
}
</style>
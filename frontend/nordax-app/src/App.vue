<template>
<div class="wrapper">
  <MainMenu /> <br/>
  <router-view/>
  </div>
</template>

<script>
import MainMenu from './components/MainMenu.vue'
export default {
  components: {MainMenu}
  
}
</script>


<style>

body {  background-image: url("../src/assets/ivars-krutainis-jTJ9-4ESzU4-unsplash.jpg");} 

#app {
  
  }
</style>

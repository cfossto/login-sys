<template>
<div class="wrapper">
  <MainMenu /> <br/>
    <div class="content-wrapper">
      <router-view/>
    </div>
  </div>
</template>

<script>
import MainMenu from './components/MainMenu.vue'
export default {
  components: {MainMenu},

  
  
}
</script>


<style>

body {  background-image: url("../src/assets/ivars-krutainis-jTJ9-4ESzU4-unsplash.jpg");}

#app {

  }

.content-wrapper{ background-color: whitesmoke; width: 300px; margin-left: auto; margin-right: auto; }
</style>

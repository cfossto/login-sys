<template>
  <div class="landing">
      <form class="login-form">
          <input v-model="email" type="text" id="username" placeholder="Username">
          <input v-model="password" type="password" id="password" placeholder="Password">
          <input type="button" @click.prevent="sendUser" placeholder="Login" value="Login">
      </form>
  </div>
</template>

<script>
export default {
  name: 'Landingpage',

  data() { return {

    }},

    methods: {
        sendUser(){
            fetch(`http://localhost:3000/login?email=${this.email}&password=${this.password}`,{
                method: "POST"})
        }
    },

    computed:{

    }

}
</script>

<style scoped>
.landing { display: flex; justify-content: center; margin-top: 15%; }
</style>
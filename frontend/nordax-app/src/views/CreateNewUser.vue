<template>
  <div class="landing">
      <form class="login-form">
          <h3>{{test}}</h3>
          <input v-model="email" type="text" name="username" id="username" placeholder="Username">
          <input v-model="password" type="password" name="password" id="password" placeholder="Password">
          <input v-model="name" type="text" name="Full name" id="name" placeholder="Full Name">
          <input type="button" @click.prevent="sendUser" placeholder="Login" value="Login">
      </form>
  </div>
</template>

<script>
export default {
    name: "Landingpage",

    data(){ return {

    }},

    methods: {
        onClick(){ 
            console.log("hej");
            },

        sendUser(){
            fetch(`http://localhost:3000/create_user?email=${this.email}&password=${this.password}&name=${this.name}`,{
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
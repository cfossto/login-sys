<template>
  <div class="landing">
      <form class="login-form">
          <h3>{{test}}</h3>
          <input v-model="email" type="text" name="username" id="username" placeholder="Username">
          <input v-model="password" type="password" name="password" id="password" placeholder="Password">
          <input @click.prevent="onClick" type="submit" value="submit" placeholder="Login">
      </form>
  </div>
</template>

<script>
export default {
    name: "Landingpage",

    data(){ return {test:"test" }},

    methods: {
        onClick(){ console.log("hej"); },
        sendUser(){
            fetch(`http://localhost:3000/create_user?email=${email}&password=${password}&name=kalle`,{metod:"POST"})
        }
    },
    computed:{

    }

}
</script>

<style scoped>
.landing { display: flex; justify-content: center; margin-top: 15%; }
</style>
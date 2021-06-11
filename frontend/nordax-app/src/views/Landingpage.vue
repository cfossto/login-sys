<template>
  <div class="landing">
      <form class="login-form">
          <input v-model="email" type="text" id="username" placeholder="Username">
          <input v-model="password" type="password" id="password" placeholder="Password">
          <input type="button" @click.prevent="sendUser" placeholder="Login" value="Login" id="sendButton">
      </form>
  </div>
  <div class="createAccount">
      <p>Need an account?</p>
      <br/>
      <p class="register-btn"><router-link to="/new_user"> Click here</router-link></p>
  </div>
</template>

<script>
export default {
  name: 'Landingpage',

  data() { return {
      success: false,
      password: "",
      email: ""

    }},

    methods: {
        async sendUser(){
            await fetch(`http://localhost:3000/login?email=${this.email}&password=${this.password}`,{
                method: "POST"})

                .then(res => { if (res.status==200){ window.location.href="/inside" }})
        }
    }

}
</script>

<style scoped>
.landing, .createAccount { display: flex; justify-content: center;  margin-top: 15%; }
.createAccount { display: flex; justify-content: center; ; }
input { height: 45px; width: 150px; border-radius: 1px; margin-top:40px; margin-bottom: 40px; display:flex; justify-content: center; }
#sendButton { color:whitesmoke; border-style: groove; height: 60px; background-color: rgb(120, 172, 96);}


</style>
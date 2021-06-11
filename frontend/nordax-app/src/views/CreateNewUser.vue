<template>
  <div class="newUserForm">
      <form class="login-form">
          <h3>{{test}}</h3>
          <input v-model="email" type="text" name="username" id="username" placeholder="Username"><br/>
          <input v-model="password" type="password" name="password" id="password" placeholder="Password"><br/>
          <input v-model="name" type="text" name="Full name" id="name" placeholder="Full Name"><br/>
          <input type="button" @click.prevent="sendUser" placeholder="Login" value="Create User">
      </form>
  </div>
</template>

<script>
export default {
    name: "Landingpage",

    data(){
        return{
        }
    },

    methods: {
        onClick(){ 
            console.log("hej");
            },

        sendUser(){
            fetch(`http://localhost:3000/create_user?email=${this.email}&password=${this.password}&name=${this.name}`,{
                method: "POST"})

                window.location.href="/"
        }
    },

    computed:{

    }

}
</script>

<style scoped>
.newUserForm { margin-top: 25%; padding: 15%; }
input { margin: 5% }
</style>
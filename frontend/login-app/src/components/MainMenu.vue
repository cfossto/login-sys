<template>
  
  <div class="mainMenu" v-if="logged_in">
      <div class="flexcontainer">
      <li>
          <ul>
              <router-link to="/inside">Home</router-link>
          </ul>
          <ul>
              <router-link to="/edit_user">Edit User</router-link>
          </ul>
          <ul @click="logout">
              <router-link to="/">Logout</router-link>
          </ul>
      </li>
      </div>
  </div>

</template>

<script>
export default {

    data(){
        return {
            logged_in: true
        }
    },
    methods: {
        logout(){
            this.logged_in = false
        }
    }


}
</script>

<style scoped>

.mainMenu { height: 10%; background-color: whitesmoke; opacity: 97%;margin-left: auto; margin-right: auto;}
li { list-style-type: none; font-size: 25px;}
ul { display: inline-block; margin-left: 18%; }


</style>
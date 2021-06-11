<template>
  
  <div class="mainMenu" v-if="logged_in">
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

.mainMenu { height: 10%; background-color: whitesmoke; opacity: 97%; display: flex; align-items: center; justify-content: center;}
li { list-style-type: none; }
ul { display: inline-block; text-decoration: underline; color: seagreen; cursor: pointer; }

</style>
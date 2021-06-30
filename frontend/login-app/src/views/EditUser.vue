<template>
  <div class="edit">
      <h1>Edit User</h1><br/>
      <h3 @click="showChangePass" >Change Password</h3>
      <form>
        <input v-model="oldPassword" type="password" name="Change password" id="change_password" placeholder="Old Password"><br/>
        <input v-model="newPassword" type="password" name="New password" id="new-password" placeholder="New Password"><br/>
        <input @click.prevent="updatePassword" type="button" value="Update Password" class="btn">
      </form>
      
      <div>
          <h3>Remove account?</h3>
          <input v-model="removePass" type="password" name="rm-account" id="rm-account" placeholder="Provide Password"><br>
          <input @click="removeAccount" type="button" value="Remove" class="btn">
      </div>

  </div>
</template>

<script>
export default {
    name: 'editUser',

    data(){
        return{
            oldPassword: this.oldPassword,
            newPassword: this.newPassword,
            removePass: "",
            changePass: false,
            Username: false,
            Name: false
        }
    },
    methods:{
        
        showChangePass(){
            this.changePass = !this.changePass;
        },
        
        updatePassword(){
            fetch(`http://localhost:3000/password/change?id=18&old-password=${this.oldPassword}&password=${this.newPassword}`,
            {method:"POST"})
            window.location.href="/inside"
        },
        removeAccount(){
            if (this.removePass == "password"){
                fetch(`http://localhost:3000//user/18`,{method:"DELETE"})
            }
            window.location.href="/"
        }


    }

}
</script>

<style scoped>
.edit { padding: 15%; margin-top: 10% }
input { margin-bottom: 10%; }
</style>
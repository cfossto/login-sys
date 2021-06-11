<template>
  <div class="edit">
      <h1>Edit User</h1><br/>
      <h3 @click="showChangePass" >Change Password</h3>
      <form v-if="changePass">
        <input v-model="oldPassword" type="password" name="Change password" id="change_password" placeholder="Old Password">
        <input v-model="newPassword" type="password" name="New password" id="new-password" placeholder="New Password">
        <input @click="updatePassword" type="button" value="Update Password">
      </form>
      
      <h3 @click="changeUsername">Change username</h3>
      <form v-if="Username">
          <input type="text" name="Change user name" id="change-username">
          <input @click="changeUsername" type="button" value="Change name">
      </form>
      
      <h3 @click="changeFullName">Change Full Name</h3>
      <form v-if="Name">
          <input type="text" name="Change full name" id="change-full-name">
      </form>

      <div>
          <h3>Remove account?</h3>
          <input v-model="removePass" type="text" name="rm-account" id="rm-account" placeholder="password">
          <p></p>
          <input @click="removeAccount" type="button" value="Remove">
      </div>

  </div>
</template>

<script>
export default {
    name: 'editUser',

    data(){
        return{
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
            fetch(`http://localhost:3000/password/change?id=6&old-password=${this.oldPassword}&password=${this.newPassword}`,
            {method:"POST"})
            window.location.href="/"
        },
        changeUsername(){
            this.Username = !this.Username;
        },
        changeFullName(){
            this.Name = !this.Name
        },
        removeAccount(){
            if (this.removePass == "password"){
                fetch(`http://localhost:3000//user/9`,{method:"DELETE"})
            }
            window.location.href="/"
        }


    }

}
</script>

<style scoped>
.edit { display: flex; flex-direction: column; justify-content:center;  align-items: center; }
h3 { cursor:pointer; }
</style>
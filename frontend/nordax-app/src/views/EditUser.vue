<template>
  <div class="edit">
      <h1>Edit User</h1><br/>
      <h3 @click="showChangePass" >Change Password</h3>
      <form>
        <input v-model="oldPassword" type="password" name="Change password" id="change_password" placeholder="Old Password"><br/>
        <input v-model="newPassword" type="password" name="New password" id="new-password" placeholder="New Password"><br/>
        <input @click.prevent="updatePassword" type="button" value="Update Password" class="btn">
      </form>
      
      <h3 @click="changeUsername">Change username</h3>
      <form>
          <input type="text" name="Change user name" id="change-username" placeholder="Add new username" ><br/>
          <input @click="changeUsername" type="button" value="Change name" class="btn">
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
        changeUsername(){
            this.Username = !this.Username;
        },
        changeFullName(){
            this.Name = !this.Name
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
.edit { display: flex; flex-direction: column; justify-content:center;  align-items: center; 
        background-color: whitesmoke; opacity: 95%; margin: 5%; width: 300px; padding: 8%;}
h3 { cursor:pointer; margin-top: 13%; }
input { margin-bottom: 1%; display: flex; justify-content: center; align-items: center;}
.btn { display: flex; justify-content: center; align-items: center; }
</style>
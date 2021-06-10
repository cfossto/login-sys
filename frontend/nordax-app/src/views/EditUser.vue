<template>
  <div class="edit">
      <h1>Edit User</h1>
      <h3 @click="showChangePass">Change Password</h3>
      <form v-if="changePass">
        <input v-model="oldPassword" type="password" name="Change password" id="change_password" placeholder="Old Password">
        <input v-model="newPassword" type="password" name="New password" id="new-password" placeholder="New Password">
        <input @click="updatePassword" type="button" value="Update Password">
      </form>
  </div>
</template>

<script>
export default {
    name: 'editUser',

    data(){
        return{
            changePass: false
        }
    },
    methods:{
        showChangePass(){
            this.changePass = !this.changePass;
        },
        updatePassword(){
            fetch(`http://localhost:3000/password/change?id=6&old-password=${this.oldPassword}&password=${this.newPassword}`,
            {method:"POST"})
        }
    }

}
</script>

<style scoped>
.edit { }
</style>
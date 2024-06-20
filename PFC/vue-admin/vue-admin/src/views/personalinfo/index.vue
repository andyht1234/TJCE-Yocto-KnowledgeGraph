<template>
  <div class="app-container">
    <el-form ref="userInfoForm" :model="userInfo" label-width="80px">
      <el-form-item label="用户名">
        <el-input v-model="userInfo.username" :disabled="!isEdit"></el-input>
      </el-form-item>
      <el-form-item label="手机号">
        <el-input v-model="userInfo.phone" :disabled="!isEdit"></el-input>
      </el-form-item>
      <el-form-item label="邮箱">
        <el-input v-model="userInfo.email" :disabled="!isEdit"></el-input>
      </el-form-item>
      <el-form-item v-if="!isEdit">
        <el-button type="primary" @click="editUserInfo">修改</el-button>
      </el-form-item>
      <el-form-item v-if="isEdit" label="原密码">
        <el-input v-model="originPassword" type="password"></el-input>
      </el-form-item>
      <el-form-item v-if="isEdit" label="新密码">
        <el-input v-model="newPassword" type="password"></el-input>
      </el-form-item>
      <el-form-item v-if="isEdit" label="确认密码">
        <el-input v-model="confirmPassword" type="password"></el-input>
      </el-form-item>
      <el-form-item v-if="isEdit">
        <el-button @click="confirmEdit">确认</el-button>
        <el-button @click="cancelEdit">取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isEdit: false,
      userInfo: {
        username: 'John Doe',
        phone: '1234567890',
        email: 'johndoe@example.com',
        password: 'password123'
      },
      originPassword: '',
      newPassword: '',
      confirmPassword: ''
    }
  },
  methods: {
    editUserInfo() {
      this.isEdit = true
    },
    confirmEdit() {
      if (this.originPassword !== this.userInfo.password) {
        this.$message.error('密码错误')
      } else if (this.newPassword !== this.confirmPassword) {
        this.$message.error('两次输入的密码不同')
      } else {
        this.$message.success('修改成功')
        this.userInfo.password = this.newPassword
        this.isEdit = false
      }
    },
    cancelEdit() {
      this.isEdit = false
    }
  }
}
</script>

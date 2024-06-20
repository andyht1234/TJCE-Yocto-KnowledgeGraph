<template>
  <div>
    <!--普通用户report界面-->
  <div v-if="userRole=='user'" class="report-form">
    <el-form ref="reportForm" :model="reportForm" label-width="80px">
      <el-form-item label="内容">
        <el-input v-model="reportForm.content" type="textarea" :rows="5" placeholder="请输入内容"></el-input>
      </el-form-item>
      <el-form-item label="版本更新">
        <el-checkbox v-model="reportForm.versionUpdate">版本更新</el-checkbox>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm">提交</el-button>
      </el-form-item>
    </el-form>
    <el-table :data="reportList" style="width: 100%">
      <el-table-column prop="id" label="ID"></el-table-column>
      <el-table-column prop="state" label="状态"></el-table-column>
      <el-table-column prop="submitTime" label="提交时间"></el-table-column>
      <!--行展开内容-->
      <el-table-column type="expand">
        <template slot-scope="scope">
          <el-form label-position="top">
            <el-form-item label="内容" :border="true">
              <span>{{scope.row.content}}</span>
            </el-form-item>
            <el-form-item v-if="scope.row.state === '已审核'" label="回复" :border="true">
              <span>{{scope.row.reply}}</span>
            </el-form-item>
          </el-form>
        </template>
      </el-table-column>
    </el-table>
  </div>

  <!--管理员report界面-->
  <div v-if="userRole === 'admin'">
      <el-table :data="adminReportList" style="width: 100%">
        <el-table-column prop="id" label="ID"></el-table-column>
        <el-table-column prop="state" label="状态"></el-table-column>
        <el-table-column prop="submitTime" label="提交时间"></el-table-column>
        <el-table-column type="expand">
          <template slot-scope="scope">
            <el-form label-position="top">
              <el-form-item label="内容" :border="true">
                <span>{{scope.row.content}}</span>
              </el-form-item>
              <el-form-item v-if="scope.row.state=='待审核'" :border="true">
                <el-button size="small" type="danger" @click="deleteReport(scope.row)">删除</el-button>
                <el-button size="small" type="warning" @click="rejectReport(scope.row)">拒绝</el-button>
                <el-button size="small" type="primary" @click="replyReport(scope.row)">回复</el-button>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <el-dialog :visible.sync="replyDialogVisible" title="回复">
      <el-input v-model="replyContent" type="textarea" :rows="4" placeholder="请输入回复内容"></el-input>
      <span slot="footer" class="dialog-footer">
        <el-button @click="replyCancel">取消</el-button>
        <el-button type="primary" @click="submitReply">提交</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userRole: 'admin',
      reportForm: {
        content: '',
        versionUpdate: false
      },
      reportList: [],
      adminReportList: [
        {
          id: 1,
          state: '待审核',
          submitTime: '2022-01-01 10:00:00',
          content: '这是管理员报告1的内容',
          reply: ''
        },
        {
          id: 2,
          state: '待审核',
          submitTime: '2022-01-02 11:00:00',
          content: '这是管理员报告2的内容',
          reply: ''
        },
        {
          id: 3,
          state: '待审核',
          submitTime: '2022-01-03 12:00:00',
          content: '这是管理员报告3的内容',
          reply: ''
        }],
      replyDialogVisible: false,
      replyContent: ''
    }
  },
  methods: {
    submitForm() {
      this.$message.success('提交成功')
      this.reportList.push({
        id: this.reportList.length + 1,
        state: '待审核',
        submitTime: new Date().toLocaleString(),
        content: this.reportForm.content,
        reply: ''
      })
      this.reportForm.content = ''
    },
    deleteReport(report) {
      report.state = '已审核'
    },
    rejectReport(report) {
      report.state = '已审核'
    },
    replyReport(report) {
      report.state = '已审核'
      this.replyDialogVisible = true
    },
    submitReply() {
      this.$message.success('提交成功')
      this.replyDialogVisible = false
    },
    replyCancel() {
      this.replyDialogVisible = false
      this.replyContent = ''
    }
  }
}
</script>

<style>
.report-form {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}
</style>

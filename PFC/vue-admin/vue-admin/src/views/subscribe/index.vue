<template>
  <div class="app-container">
    <el-table
      v-loading="listLoading"
      :data="list"
      element-loading-text="Loading"
      border
      fit
      highlight-current-row
    >
      <el-table-column align="center" label="Ranking" width="95">
        <template slot-scope="scope">
          {{ scope.$index + 1 }}
        </template>
      </el-table-column>
      <el-table-column label="Organization" width="350" align="center">
        <template slot-scope="scope">
          {{ scope.row.organization }}
        </template>
      </el-table-column>
      <el-table-column label="Active Contribution" width="200" align="center">
        <template slot-scope="scope">
          <span>{{ scope.row.active_contribution }}</span>
        </template>
      </el-table-column>
      <el-table-column label="Total Community" width="150" align="center">
        <template slot-scope="scope">
          {{ scope.row.total_community }}
        </template>
      </el-table-column>
      <el-table-column label="Operation" width="200" align="center">
        <template slot-scope="scope">
          <el-button size="small" @click="showTipsDialog(scope.row)">{{ scope.row.tips ? 'Modify' : 'AddTips' }}</el-button>
          <el-button size="small" type="danger" @click="deleteRow(scope.$index)">Delete</el-button>
        </template>
      </el-table-column>
      <el-table-column type="expand" :expand="expandRow">
        <template slot-scope="scope">
          <div v-if="scope.row.tips">{{ scope.row.tips }}</div>
          <div v-else>No tips available</div>
        </template>
      </el-table-column>
    </el-table>
    <el-dialog
      :visible.sync="dialogVisible"
      title="Add/Edit Tips"
      width="30%"
      :before-close="handleDialogClose"
    >
      <el-input v-model="tipsInput" placeholder="Enter tips here"></el-input>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">Cancel</el-button>
        <el-button type="primary" @click="submitTips">Submit</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  data() {
    return {
      listLoading: false,
      list: [
        { organization: 'Organization A', active_contribution: 100, total_community: 500, tips: '' },
        { organization: 'Organization B', active_contribution: 150, total_community: 700, tips: 'Good performance' },
        { organization: 'Organization C', active_contribution: 80, total_community: 300, tips: 'Needs improvement' }
      ],
      dialogVisible: false,
      tipsInput: '',
      currentRow: null
    }
  },
  methods: {
    showTipsDialog(row) {
      this.dialogVisible = true
      this.currentRow = row
      this.tipsInput = row.tips
    },
    handleDialogClose(done) {
      this.$confirm('Are you sure to close the dialog?')
        .then(_ => {
          done()
        })
        .catch(_ => {})
    },
    submitTips() {
      this.currentRow.tips = this.tipsInput
      this.dialogVisible = false
      this.$message.success('Tips added/updated successfully')
    },
    deleteRow(index) {
      this.$confirm('Are you sure to delete this record?')
        .then(_ => {
          this.list.splice(index, 1)
          this.$message.success('Record deleted successfully')
        })
        .catch(_ => {})
    },
    expandRow(row, expandedRows) {
      return expandedRows.includes(row)
    }
  }
}
</script>

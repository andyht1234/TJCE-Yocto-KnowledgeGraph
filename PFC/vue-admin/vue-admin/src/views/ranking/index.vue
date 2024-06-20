
<template>
  <div>
    <!--月榜、日榜切换-->
    <el-header>
      <el-menu :default-active="activeIndex" mode="horizontal" @select="handleMenuSelect">
        <el-menu-item index="monthly">Monthly</el-menu-item>
        <el-menu-item index="daily">Daily</el-menu-item>
      </el-menu>
    </el-header>

    <el-container>
      <!--top语言排行-->
      <div style="float: left; margin-left: 20px;">
        <h2>TOP Language</h2>
        <el-table
          :data="topLanguagesData"
          style="width: 300px;">
          <el-table-column prop="language" label="Language"></el-table-column>
          <el-table-column prop="proportion" label="Proportion"></el-table-column>
        </el-table>
      </div>

    <el-main style="width: calc(100% - 200px); padding: 20px;">
      <!--表单筛选-->
      <el-form :model="filterForm" inline>
        <el-form-item label="Organization">
    <el-select v-model="filterForm.organization" multiple placeholder="Select" style="width: 150px">
      <el-option label="Organization 1" value="org1"></el-option>
      <el-option label="Organization 2" value="org2"></el-option>
    </el-select>
  </el-form-item>
  <el-form-item label="Industry">
    <el-select v-model="filterForm.industry" multiple placeholder="Select" style="width: 100px">
      <el-option label="Industry 1" value="ind1"></el-option>
      <el-option label="Industry 2" value="ind2"></el-option>
    </el-select>
  </el-form-item>
  <el-form-item label="Month">
    <el-select v-model="filterForm.month" placeholder="Select" style="width: 100px">
      <el-option label="January" value="January"></el-option>
      <el-option label="February" value="February"></el-option>
      <el-option label="March" value="March"></el-option>
    </el-select>
  </el-form-item>
  <el-form-item label="Year">
    <el-select v-model="filterForm.year" placeholder="Select" style="width: 100px">
      <el-option label="2022" value="2022"></el-option>
      <el-option label="2023" value="2023"></el-option>
      <el-option label="2024" value="2024"></el-option>
    </el-select>
  </el-form-item>
      </el-form>

      <!--排行榜主体-->
      <el-table :data="tableData.slice((currentPage-1)*10,currentPage*10)" style="width: 100%" :row-key="row => row.rank">
        <el-table-column prop="rank" label="Rank"></el-table-column>
        <el-table-column prop="organization" label="Organization"></el-table-column>
        <el-table-column prop="activeContributors" label="Active Contributors"></el-table-column>
        <el-table-column prop="totalCommunity" label="Total Community"></el-table-column>
        <el-table-column type="expand">
          <template #default="{ row }">
            <el-row>
              <el-col :span="8">
                <p><b>Active User</b></p>
                <ul>
                  <li>Name: {{ row.activeUser.name }}</li>
                  <li>Frequency: {{ row.activeUser.frequency }}</li>
                  <li>Type: {{ row.activeUser.type }}</li>
                  <li>Organization: {{ row.activeUser.organization }}</li>
                </ul>
              </el-col>
              <el-col :span="8">
                <p><b>Top Languages</b></p>
                <ul>
                  <li>{{ row.topLanguages }}</li>
                </ul>
              </el-col>
              <el-col :span="8">
                <p><b>Bug Analysis</b></p>
                <ul>
                  <li>Done Num: {{ row.bugAnalysis.doneNum }}</li>
                  <li>Todo Num: {{ row.bugAnalysis.todoNum }}</li>
                </ul>
              </el-col>
              <el-col :span="8">
                <p><b>Enterprise User</b></p>
                <ul>
                  <li>{{ row.enterpriseUser }}</li>
                </ul>
              </el-col>
              <el-col :span="8">
                <p><b>Leading Organization</b></p>
                <ul>
                  <li>{{ row.leadingOrganization }}</li>
                </ul>
              </el-col>
              <el-col :span="8">
                <p><b>Project Owner</b></p>
                <ul><li>{{ row.projectOwner }}</li>
                </ul>
              </el-col>
              <el-col :span="8">
                <p><b>License Usage</b></p>
                <ul>
                  <li>{{ row.licenseUsage }}</li>
                </ul>
              </el-col>
              <el-col :span="8">
                <p><b>Versions</b></p>
                <ul>
                  <li><a :href="row.versions.link">{{ row.versions.name }}</a></li>
                </ul>
              </el-col>
            </el-row>
          </template>
        </el-table-column>
      </el-table>

      <el-pagination
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-size="10"
        layout="prev, pager, next"
        :total="tableData.length"
      ></el-pagination>
    </el-main>
  </el-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeIndex: 'monthly',
      filterForm: {
        organization: [],
        industry: [],
        month: [],
        year: []
      },
      tableData: [
        {
          rank: 1,
          organization: 'Organization1',
          activeContributors: 100,
          totalCommunity: 1000,
          emailAddress: 'organization1@example.com',
          activeUser: {
            name: 'John Doe',
            frequency: 'Daily',
            type: 'Admin',
            organization: 'Organization1'
          },
          topLanguages: 'JavaScript, Python, Java',
          enterpriseUser: 'Yes',
          bugAnalysis: {
            doneNum: 20,
            todoNum: 5
          },
          leadingOrganization: 'Organization1',
          projectOwner: 'Jane Smith',
          licenseUsage: 'MIT License',
          versions: {
            name: 'Version 1.0',
            link: 'https://example.com/version1'
          }
        },
        {
          rank: 2,
          organization: 'Organization2',
          activeContributors: 90,
          totalCommunity: 900,
          emailAddress: 'organization2@example.com',
          activeUser: {
            name: 'Alice Johnson',
            frequency: 'Weekly',
            type: 'User',
            organization: 'Organization2'
          },
          topLanguages: 'Java, C++, Ruby',
          enterpriseUser: 'No',
          bugAnalysis: {
            doneNum: 15,
            todoNum: 3
          },
          leadingOrganization: 'Organization2',
          projectOwner: 'Bob Brown',
          licenseUsage: 'Apache License',
          versions: {
            name: 'Version 2.0',
            link: 'https://example.com/version2'
          }
        }
        // Add more data here
      ],
      currentPage: 1
    }
  },
  methods: {
    handleMenuSelect(index) {
      this.activeIndex = index
      // Handle switching monthly and daily rankings
    },
    handleCurrentChange(val) {
      this.currentPage = val
    }
  }
}
</script>

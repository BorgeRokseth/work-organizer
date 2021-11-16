<template>
  <v-container>
    <v-card>
      <v-card-title>Projects</v-card-title>
      <v-card-text>
        <v-simple-table dark>
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">Name</th>
                <th class="text-left">Goal</th>
                <th class="text-left">Date</th>
                <th></th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="project in activeProjects" :key="project.id">
                <td>{{ project.name }}</td>
                <td>{{ project.goal }}</td>
                <td>{{ project.created }}</td>
                <td>
                  <v-icon small @click="editProject(project)">
                    mdi-pencil
                  </v-icon>
                </td>
                <td>
                  <v-icon small @click="archiveProject(project)">
                    mdi-check-outline
                  </v-icon>
                </td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-card-text>
      <v-card-actions>
        <v-btn dark @click="newProject()">New project</v-btn>
      </v-card-actions>
    </v-card>
    <project-detail-dialog
      :show-dialog="showProjectDetailDialog"
      :project-id="editedProjectId"
      :project-name="editedProjectName"
      :goal="editedProjectGoal"
      :actions="editedProjectActions"
      :title="dialogTitle"
      @close:dialog="closeProjectDetailDialog"
    />
  </v-container>
</template>

<script>
import { apiService } from "@/common/api.service";
import ProjectDetailDialog from "../components/ProjectDetails.vue";
export default {
  name: "ProjectList",
  components: { ProjectDetailDialog },
  data() {
    return {
      activeProjects: [],
      showProjectDetailDialog: false,
      editedProjectId: null,
      editedProjectName: "",
      editedProjectGoal: "",
      editedProjectActions: [],
      dialogTitle: ""
    };
  },
  methods: {
    getActiveProjects() {
      const endpoint = "/api/next-actions/active-projects/";
      const method = "GET";
      apiService(endpoint, method).then((data) => {
        this.activeProjects = data;
      });
    },
    editProject(project) {
      console.log("Edit project: ", project.name);
    },
    archiveProject(project) {
      console.log("Archive project: ", project.name);
    },
    closeProjectDetailDialog() {
      this.showProjectDetailDialog = false;
    },
    newProject() {
        this.dialogTitle = "Create New Project";
        this.editedProjectId = null;
        this.editedProjectName = "";
        this.editedProjectGoal = "";
        this.editedProjectActions = [];

        this.showProjectDetailDialog = true;
    }
  },
  created() {
    this.getActiveProjects();
  },
};
</script>

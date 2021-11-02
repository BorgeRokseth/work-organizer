<template>
  <div>
    <v-expansion-panels dark>
      <v-expansion-panel v-for="item in contextItems" :key="item.id">
        <v-expansion-panel-header>{{ item.name }}</v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-expansion-panels>
            <v-expansion-panel
              v-for="project in activeProjects"
              :key="project.id"
            >
              <v-expansion-panel-header
                v-if="projectHasActionWithContext(project, item.id)"
                >{{ project.name }}</v-expansion-panel-header
              >
              <v-expansion-panel-content
                v-for="action in project.actions"
                :key="action"
              >
                {{ action }}
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service";
export default {
  name: "NextActionList",
  components: {},
  data() {
    return {
      contextItems: [],
      activeProjects: [],
      nextAction: null,
    };
  },
  methods: {
    getContextItems() {
      const endpoint = "/api/next-actions/contexts/";
      const method = "GET";
      apiService(endpoint, method).then((data) => {
        this.contextItems = data;
      });
    },
    getActiveProjects() {
      const endpoint = "/api/next-actions/active-projects/";
      const method = "GET";
      apiService(endpoint, method).then((data) => {
        this.activeProjects = data;
      });
    },
    getNextActionItem(id) {
      const endpoint = `/api/next-actions/next-actions/${id}/`;
      const method = "GET";
      apiService(endpoint, method).then((data) => {
        this.nextAction = data;
      });
    },
    projectHasActionWithContext(project, context) {
      console.log("Context: ", context);
      console.log("Project: ", project.name);
      for (const actionId of project.actions) {
        this.getNextActionItem(actionId);
        if (this.nextAction !== undefined){
            console.log("Action ID: ", this.nextAction);
        }
      }
      return true;
    },
  },
  created() {
    this.getContextItems();
    this.getActiveProjects();
  },
};
</script>

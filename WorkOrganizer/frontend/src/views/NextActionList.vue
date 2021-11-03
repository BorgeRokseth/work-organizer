<template>
  <v-col>
    <v-expansion-panels>
      <v-expansion-panel v-for="item in contextItems" :key="item.id">
        <v-expansion-panel-header><h2>{{ item.name }}</h2></v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-expansion-panels dark>
            <v-expansion-panel
              v-for="project in activeProjects"
              :key="project.id" popout dark
            >
              <v-expansion-panel-header
                v-if="projectHasActionWithContext(project, item.id)" 
                ><h3>{{ project.name }}</h3></v-expansion-panel-header
              >
              <v-expansion-panel-content
                v-for="action in project.actions"
                :key="action.id"
              >
                <div v-if="actionBelongsToContext(action, item.id)">
                  {{ action.description }}
                </div>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </v-col>
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
      nextActions: [],
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
    getNextActions() {
      const endpoint = "/api/next-actions/next-actions/";
      const method = "GET";
      apiService(endpoint, method).then((data) => {
        this.nextActions = data;
      });
    },
    projectHasActionWithContext(project, context) {
      let hasActionWithContext = false;
      for (const action of project.actions) {
        if (action.context === context) {
          hasActionWithContext = true;
        }
      }
      return hasActionWithContext;
    },
    actionBelongsToContext(action, context) {
      if (action.context === context) {
        return true;
      } else {
        return false;
      }
    },
  },
  created() {
    this.getContextItems();
    this.getActiveProjects();
  },
};
</script>

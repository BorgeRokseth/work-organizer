<template>
  <v-container>
    <h2>Next actions</h2>
    <v-card v-for="context in contextItems" :key="context.id" class="mt-2">
      <v-card-title>{{ context.name }}</v-card-title>
      <v-card-text>
        <v-simple-table dark>
          <template v-slot:default>
            <thead>
              <tr>
                <th class="text-left">Description</th>
                <th class="text-left">Project</th>
                <th class="text-left">Date</th>
                <th class="text-left">Done</th>
              </tr>
            </thead>
            <tbody>
              <tr
                v-for="action in nextActiveActionByContext(context.id)"
                :key="action.id"
              >
                <td>{{ action.description }}</td>
                <td>{{ action.project[0] }}</td>
                <td>{{ action.created }}</td>
                <td>
                  <v-icon
                    small
                    @click="
                      deleteNextAction(
                        action.id,
                        action.description,
                        action.project[0],
                        context.id
                      )
                    "
                  >
                    mdi-check-outline
                  </v-icon>
                </td>
              </tr>
              <tr>
                <td>
                  <v-text-field
                    label="New Next Action"
                    v-model="newActionDescription"
                  ></v-text-field>
                </td>
                <td>proj yes?</td>
                <td>-</td>
                <td>
                  <v-icon small @click="newNextAction(context.id)">
                    mdi-plus-box
                  </v-icon>
                </td>
              </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-card-text>
    </v-card>
  </v-container>
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
      newActionDescription: "",
      editedProjectData: null,
      newActionProjectId: 2,
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
    nextActiveActionByContext(contextId) {
      const listOfActions = [];
      for (const action of this.nextActions) {
        if (action.context === contextId && action.done !== true) {
          listOfActions.push(action);
        }
      }
      return listOfActions;
    },
    deleteNextAction(id, description, project, contextId) {
      const endpoint = `/api/next-actions/next-actions/${id}/`;
      const method = "PUT";
      const data = {
        description: description,
        context: contextId,
        done: true,
      };
      apiService(endpoint, method, data).then(() => this.getNextActions());
    },
    newNextAction(contextId) {
      const endpoint = "/api/next-actions/next-actions/";
      const method = "POST";
      const data = {
        description: this.newActionDescription,
        context: contextId,
        done: false,
      };
      this.newActionDescription = "";
      apiService(endpoint, method, data).then((data) => {
        if (this.newActionProjectId !== null) {
          this.updateProject(data);
        }
        this.newActionDescription = "";
      });
    },
    updateProject(newNextAction) {
      const endpoint = `/api/next-actions/project/${this.newActionProjectId}/`;
      apiService(endpoint, "GET").then((data) => {
        this.editedProjectData = data;
        let actionIsNotInProject = true;
        for (const action of this.editedProjectData.actions) {
          if (action.id === newNextAction.id) {
            actionIsNotInProject = false;
          }
        }
        if (actionIsNotInProject) {
          this.editedProjectData.actions.push(newNextAction);
        }
        apiService(endpoint, "PUT", this.editedProjectData).then(
          () => this.getNextActions
        );
      });
    },
  },
  created() {
    this.getContextItems();
    this.getActiveProjects();
    this.getNextActions();
  },
};
</script>

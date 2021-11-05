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
                <td>{{ action.project }}</td>
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
                <td>put in v-select</td>
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
        project: 2,
        done: false,
      };
      apiService(endpoint, method, data).then(() =>{
        this.getNextActions();
        this.newActionDescription = "";
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

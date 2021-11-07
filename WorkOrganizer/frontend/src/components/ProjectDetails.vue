<template>
  <v-row justify="center">
    <v-dialog v-model="showDialog" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">{{ title }}</span>
        </v-card-title>
        <v-card-text>
          <v-text-field
            v-model="projectNewName"
            label="Project Name"
            outlined
            clearable
          ></v-text-field>
          <v-textarea
            outlined
            label="Project Goal"
            v-model="projectNewGoal"
          ></v-textarea>
          <v-list>
            <v-header>Actions</v-header>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title
                  >Første action lagt til prosjekt</v-list-item-title
                >
              </v-list-item-content>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title>En annen action...</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list>
        </v-card-text>
        <v-card-actions>
          <v-btn color="blue darken-1" @click="closeDialog()"> Close </v-btn>
          <v-btn color="blue darken-1"> Save </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  name: "",
  props: {
    showDialog: Boolean,
    projectId: { type: [Number, null] },
    projectName: String,
    goal: String,
    actions: Array,
    title: String,
  },
  data() {
    return {
      projectNewName: "",
      projectNewGoal: "",
    };
  },
  methods: {
    closeDialog() {
      this.$emit("close:dialog", {});
    },
    initializeVariables() {
      this.projectNewName = this.projectName;
      this.projectNewGoal = this.goal;
    },
  },
  created() {
    this.initializeVariables();
  },
};
</script>

<style scoped></style>

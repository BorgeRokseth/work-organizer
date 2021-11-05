<template>
  <v-container>
    <h2>Projects</h2>
  </v-container>
</template>

<script>
import { apiService } from "@/common/api.service";
export default {
  name: "ProjectList",
  components: {},
  data() {
    return {
      activeProjects: [],
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
  },
  created() {
    this.getActiveProjects();
  },
};
</script>
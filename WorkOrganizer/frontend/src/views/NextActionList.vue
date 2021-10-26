<template>
  <div>
    <v-expansion-panels focusable>
      <v-expansion-panel v-for="item in contextItems" :key="item.id">
        <v-expansion-panel-header>{{item.name}}</v-expansion-panel-header>
        <v-expansion-panel-content>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat.
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
  },
  created() {
    this.getContextItems();
  },
};
</script>

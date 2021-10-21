<template>
  <div>
      <v-container>
          <h1> Inbox </h1>
            <v-data-table 
                v-model="selectedItems"
                :headers="headers" 
                :items="inboxItems" 
                :items-per-page="20" 
                show-select
                class="elevation-1"
            ></v-data-table>
      </v-container>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service";

export default {
  name: "Inbox",
  components: {
  },
  data() {
      return {
          inboxItems: [],
          user: null,
          userId: null,
          selectedItems: [],
          headers: [
          {
            text: 'Description',
            align: 'start',
            sortable: false,
            value: 'description',
          },
          { text: 'Date', value: 'updated_date' },
        ],
      }
  },
  methods: {
    getInboxItems() {
      const endpoint = "/api/stuff/";
      apiService(endpoint).then(data => {
        this.inboxItems = data;
      });
    },
  },
  created() {
    this.getInboxItems();
  }


  
};
</script>
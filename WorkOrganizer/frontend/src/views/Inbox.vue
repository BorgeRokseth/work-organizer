<template>
  <div>
    <v-container>
      <h1>Inbox</h1>
      <v-simple-table dark>
        <template v-slot:default>
          <thead>
            <tr>
              <th class="text-left">Description</th>
              <th class="text-left">Date</th>
              <th class="text-left">Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in inboxItems" :key="item.id">
              <td>{{ item.description }}</td>
              <td>{{ item.updated_date }}</td>
              <td>
                <v-icon small @click="deleteInboxItem(item.id)">
                  mdi-delete
                </v-icon>
              </td>
            </tr>
            <tr>
              <td>
                <v-text-field
                  label="Add item"
                  v-model="newInboxItemDescription"
                ></v-text-field>
              </td>
              <td></td>
              <td>
                <v-icon small @click="addNewInboxItem()"> mdi-plus-box </v-icon>
              </td>
            </tr>
          </tbody>
        </template>
      </v-simple-table>
    </v-container>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service";

export default {
  name: "Inbox",
  components: {},
  data() {
    return {
      inboxItems: [],
      user: null,
      userId: null,
      newInboxItemDescription: "",
      headers: [
        {
          text: "Description",
          align: "start",
          sortable: false,
          value: "description",
        },
        { text: "Date", value: "updated_date" },
        { text: "Actions", value: "actions", sortable: false },
      ],
    };
  },
  methods: {
    getInboxItems() {
      const endpoint = "/api/stuff/";
      apiService(endpoint).then((data) => {
        this.inboxItems = data;
      });
    },
    deleteInboxItem(id) {
      const endpoint = `/api/stuff/${id}/`;
      const method = "DELETE";
      apiService(endpoint, method).then(this.getInboxItems());
    },
    addNewInboxItem() {
      const data = {
        description: this.newInboxItemDescription,
      };
      const endpoint = "/api/stuff/";
      const method = "POST";
      apiService(endpoint, method, data).then(this.getInboxItems());
      this.newInboxItemDescription = "";
    },
  },
  created() {
    this.getInboxItems();
  },
};
</script>

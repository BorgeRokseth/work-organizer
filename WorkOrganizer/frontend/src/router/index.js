import Vue from "vue";
import VueRouter from "vue-router";
import Inbox from "../views/Inbox.vue";
import NextActionList from "../views/NextActionList.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/inbox",
    name: "Inbox",
    component: Inbox,
  },
  {
    path: "/next-action",
    name: "NextActionList",
    component: NextActionList,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;

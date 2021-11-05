import Vue from "vue";
import VueRouter from "vue-router";
import Inbox from "../views/Inbox.vue";
import NextActionList from "../views/NextActionList.vue";
import ProjectList from "../views/ProjectList.vue"

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
  {
    path: "/projects",
    name: "ProjectList",
    component: ProjectList,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;

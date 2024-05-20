import { createWebHistory, createRouter } from "vue-router";

import InvestorsTable from "./components/InvestorsTable.vue";
import CapitalCallsTable from "./components/CapitalCallsTable.vue";
import BillsTable from "./components/BillsTable.vue";

const routes = [
  { path: "/investors", component: InvestorsTable },
  { path: "/capital-calls", component: CapitalCallsTable },
  { path: "/bills", component: BillsTable },
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});

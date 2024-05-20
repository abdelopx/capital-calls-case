import { createApp } from "vue";
import Antd from "ant-design-vue";

import "./style.css";
import "ant-design-vue/dist/reset.css";

import App from "./App.vue";
import { router } from "./router";

createApp(App).use(Antd).use(router).mount("#app");

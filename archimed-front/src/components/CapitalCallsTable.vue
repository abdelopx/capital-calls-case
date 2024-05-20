<template>
  <AddCapitalCall @refresh-capital-calls="getAllCapitalCalls" class="w-full flex justify-end" />
  <a-table class="mt-6" :loading="isLoading" :columns="columns" :data-source="capitalCalls" />
</template>
<script lang="ts" setup>
import type { TableColumnType } from "ant-design-vue";
import AddCapitalCall from "./AddCapitalCall.vue";
import { getAllCapitalBills, ICapitalCalls } from "../api/capitalCalls";
import { onMounted, ref } from "vue";

const isLoading = ref(false);
const capitalCalls = ref<ICapitalCalls[]>();

onMounted(async () => {
  getAllCapitalCalls();
});

async function getAllCapitalCalls() {
  isLoading.value = true;
  capitalCalls.value = await getAllCapitalBills();
  isLoading.value = false;
}

const columns: TableColumnType<ICapitalCalls>[] = [
  {
    title: "Total Amount",
    dataIndex: "total_amount",
  },
  {
    title: "Status",
    dataIndex: "status",
  },
  {
    title: "Investor Id",
    dataIndex: "investor",
  },
  {
    title: "Bills",
    dataIndex: "bills",
    customRender(i: any) {
      return Object.values(i.value).toString();
    },
  },
];
</script>

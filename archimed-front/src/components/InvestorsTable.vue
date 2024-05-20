<template>
  <AddInvestorModal @refresh-investors="fetchAllInvestors" class="w-full flex justify-end" />
  <a-table class="mt-6" :loading="isLoading" :columns="columns" :data-source="investors" />
</template>
<script lang="ts" setup>
import type { TableColumnType } from "ant-design-vue";
import { getAllInvestors, IInvestor } from "../api/investors";
import { onMounted, ref } from "vue";
import AddInvestorModal from "./AddInvestorModal.vue";

const isLoading = ref(false);
const investors = ref<IInvestor[]>();

onMounted(async () => {
  fetchAllInvestors();
});

async function fetchAllInvestors() {
  isLoading.value = true;
  investors.value = await getAllInvestors();
  isLoading.value = false;
}

const columns: TableColumnType<IInvestor>[] = [
  {
    title: "Name",
    dataIndex: "name",
  },
  {
    title: "IBAN",
    dataIndex: "iban",
  },
  {
    title: "Email",
    dataIndex: "email",
  },
  {
    title: "Added on",
    dataIndex: "joined_on",
  },
];
</script>

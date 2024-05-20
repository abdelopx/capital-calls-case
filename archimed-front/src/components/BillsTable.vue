<template>
  <AddBillModal @refresh-bills="fetchAllbills" class="w-full flex justify-end" />
  <a-table class="mt-6" :loading="isLoading" :columns="columns" :data-source="bills" />
</template>
<script lang="ts" setup>
import type { TableColumnType } from "ant-design-vue";
import { getAllBills, IBill } from "../api/bills";
import { onMounted, ref } from "vue";
import AddBillModal from "./AddBillModal.vue";

const isLoading = ref(false);
const bills = ref<IBill[]>();

onMounted(async () => {
  fetchAllbills();
});

async function fetchAllbills() {
  isLoading.value = true;
  bills.value = await getAllBills();
  isLoading.value = false;
}

const columns: TableColumnType<IBill>[] = [
  {
    title: "Name",
    dataIndex: "name",
  },
  {
    title: "Bill Type",
    dataIndex: "bill_type",
  },
  {
    title: "Amount",
    dataIndex: "amount",
  },

  {
    title: "Due date",
    dataIndex: "due_date",
  },
  {
    title: "Investor Id",
    dataIndex: "investor",
  },
];
</script>

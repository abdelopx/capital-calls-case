<template>
  <AddBillModal @refresh-bills="fetchAllbills" class="w-full flex justify-end" />
  <a-table @change="handleTableChange" class="mt-6" :loading="isLoading" :columns="columns" :data-source="bills" />
</template>
<script lang="ts" setup>
import { getAllBills, IBill } from "../api/bills";
import { computed, onMounted, ref } from "vue";
import AddBillModal from "./AddBillModal.vue";
import { TableProps } from "ant-design-vue";

const isLoading = ref(false);
const bills = ref<IBill[]>([]);
const billsBackup = ref<IBill[]>([]);

onMounted(async () => {
  await fetchAllbills();
  billsBackup.value = bills.value;
});

async function fetchAllbills() {
  isLoading.value = true;
  bills.value = await getAllBills();

  isLoading.value = false;
}

const columns = computed(() => [
  {
    title: "Bill Name",
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
    filters: getAvailableInvestors.value,
  },
]);

const getAvailableInvestors = computed(() =>
  billsBackup.value.reduce((acc: any[], bill) => {
    const investor = bill.investor;
    const existing = acc.find((obj) => obj.text === investor);

    if (!existing) {
      acc.push({ text: investor, value: investor });
    }
    return acc;
  }, [])
);

const handleTableChange: TableProps["onChange"] = (_, filters) => {
  bills.value = billsBackup.value;
  console.log(filters);
  bills.value = bills.value.filter((bill) => {
    if (filters.investor == null) {
      return billsBackup.value;
    } else if (filters.investor.includes(bill.investor!) && filters.investor.length > 0) {
      return bill;
    }
  });
};
</script>

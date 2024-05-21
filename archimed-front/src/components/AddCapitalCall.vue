<template>
  <div>
    <a-button type="primary" @click="showModal">Add Capital Call</a-button>
    <a-modal footer="" v-model:open="open" title="Add a new capital bill">
      <a-form
        :model="formState"
        name="basic"
        :label-col="{ span: 8 }"
        :wrapper-col="{ span: 16 }"
        autocomplete="off"
        @finish="onFinish"
        @finishFailed="onFinishFailed"
      >
        <a-form-item label="Status" name="status" :rules="[{ required: true }]">
          <a-select ref="select" v-model:value="formState.status">
            <a-select-option value="validated">Validated</a-select-option>
            <a-select-option value="sent">Sent</a-select-option>
            <a-select-option value="paid">Paid</a-select-option>
            <a-select-option value="overdue">Overdue</a-select-option>
          </a-select>
        </a-form-item>

        <a-form-item label="Date" name="due_date" :rules="[{ required: true, message: 'Please input an email' }]">
          <a-date-picker format="YYYY-MM-DD" v-model:value="formState.due_date" />
        </a-form-item>

        <a-form-item label="Investor" name="investor" :rules="[{ required: true, message: 'Please select an Investor' }]">
          <a-select ref="select" v-model:value="formState.investor">
            <a-select-option v-for="investor in investors" :value="investor.id">{{ investor.name }}</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="Bills" name="bills" :rules="[{ required: true, message: 'Please select a bill' }]">
          <a-select
            :value="formState.bills"
            mode="tags"
            style="width: 100%"
            placeholder="Please select"
            :options="availableBills.map((bill) => ({ value: bill }))"
            @change="handleChange"
          ></a-select>
        </a-form-item>

        <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
          <a-button :loading="isLoading" type="primary" html-type="submit">Add Capical Call</a-button>
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>
<script lang="ts" setup>
import { ref, defineEmits, onMounted } from "vue";
import { reactive } from "vue";
import { addCapitalCall } from "../api/capitalCalls";

import { getAllBills } from "../api/bills";
import { getAllInvestors, IInvestor } from "../api/investors";

const emit = defineEmits(["refresh-capital-calls"]);

interface FormState {
  status: string;
  investor: number | null;
  bills: number[];
  due_date: string;
}
const formState = reactive<FormState>({
  status: "",
  investor: null,
  bills: [],
  due_date: ""
});
const open = ref<boolean>(false);
const isLoading = ref(false);
const investors = ref<IInvestor[]>([]);
const availableBills = ref<number[]>([]);

const showModal = () => {
  open.value = true;
};

onMounted(async () => {
  fetchAllInvestors();
  availableBills.value = (await getAllBills()).map((bill) => bill.id);
});

async function fetchAllInvestors() {
  investors.value = await getAllInvestors();
}

const onFinish = async (values: any) => {
  isLoading.value = true;
  await addCapitalCall(values);
  isLoading.value = false;
  emit("refresh-capital-calls");
  open.value = false;
};

const onFinishFailed = (errorInfo: any) => {
  console.log("Failed:", errorInfo);
};

const handleChange = (value: number[]) => {
  formState.bills = value;
};
</script>

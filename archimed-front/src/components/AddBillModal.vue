<template>
  <div>
    <a-button type="primary" @click="showModal">Add Bill</a-button>
    <a-modal footer="" v-model:open="open" title="Add a new bill">
      <a-form
        :model="formState"
        name="basic"
        :label-col="{ span: 8 }"
        :wrapper-col="{ span: 16 }"
        autocomplete="off"
        @finish="onFinish"
        @finishFailed="onFinishFailed"
      >
        <a-form-item label="Bill Type" name="bill_type" :rules="[{ required: true }]">
          <a-select ref="select" v-model:value="formState.bill_type">
            <a-select-option value="yearly_fees">Yearly Fees</a-select-option>
            <a-select-option value="upfront_fees">Upfront Fees</a-select-option>
          </a-select>
        </a-form-item>
        <a-form-item label="Amount" name="amount" :rules="[{ required: true, message: 'Please input an amount' }]">
          <a-input v-model:value="formState.amount" />
        </a-form-item>
        <a-form-item label="Name" name="name" :rules="[{ required: true, message: 'Please input a name' }]">
          <a-input v-model:value="formState.name" />
        </a-form-item>

        <a-form-item label="Date" name="due_date" :rules="[{ required: true, message: 'Please input an email' }]">
          <a-date-picker format="YYYY-MM-DD" v-model:value="formState.due_date" />
        </a-form-item>

        <a-form-item label="Investor" name="investor" :rules="[{ required: true, message: 'Please select an Investor' }]">
          <a-select ref="select" v-model:value="formState.investor">
            <a-select-option v-for="investor in investors" :value="investor.id">{{ investor.name }}</a-select-option>
          </a-select>
        </a-form-item>

        <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
          <a-button :loading="isLoading" type="primary" html-type="submit">Add Bill</a-button>
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>
<script lang="ts" setup>
import { ref, defineEmits, onMounted } from "vue";
import { reactive } from "vue";
import { addBill } from "../api/bills";
import { getAllInvestors, IInvestor } from "../api/investors";

const emit = defineEmits(["refresh-bills"]);

interface FormState {
  amount: number | null;
  name: string;
  due_date: any;
  bill_type: string;
  investor: number | null;
}

const open = ref<boolean>(false);
const isLoading = ref(false);
const investors = ref<IInvestor[]>([]);

const showModal = () => {
  open.value = true;
};

onMounted(() => {
  fetchAllInvestors();
});

async function fetchAllInvestors() {
  investors.value = await getAllInvestors();
}

const formState = reactive<FormState>({
  amount: null,
  name: "",
  due_date: "",
  bill_type: "",
  investor: null,
});
const onFinish = async (values: any) => {
  isLoading.value = true;
  await addBill(values);
  isLoading.value = false;
  emit("refresh-bills");
  open.value = false;
};

const onFinishFailed = (errorInfo: any) => {
  console.log("Failed:", errorInfo);
};
</script>

<template>
  <div>
    <a-button type="primary" @click="showModal">Add Investor</a-button>
    <a-modal footer="" v-model:open="open" title="Add a new Investor">
      <a-form
        :model="formState"
        name="basic"
        :label-col="{ span: 8 }"
        :wrapper-col="{ span: 16 }"
        autocomplete="off"
        @finish="onFinish"
        @finishFailed="onFinishFailed"
      >
        <a-form-item label="Name" name="name" :rules="[{ required: true, message: 'Please input a name' }]">
          <a-input v-model:value="formState.name" />
        </a-form-item>

        <a-form-item label="Email" name="email" :rules="[{ required: true, message: 'Please input an email' }]">
          <a-input v-model:value="formState.email" />
        </a-form-item>

        <a-form-item label="IBAN" name="iban" :rules="[{ required: true, message: 'Please input a correct IBAN' }]">
          <a-input v-model:value="formState.iban" />
        </a-form-item>

        <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
          <a-button :loading="isLoading" type="primary" html-type="submit">Add Investor</a-button>
        </a-form-item>
      </a-form>
    </a-modal>
  </div>
</template>
<script lang="ts" setup>
import { ref, defineEmits } from "vue";
import { reactive } from "vue";
import addInvestor from "../api/investors";

const emit = defineEmits(["refresh-investors"]);

interface FormState {
  name: string;
  email: string;
  iban: string;
}

const open = ref<boolean>(false);
const isLoading = ref(false);

const showModal = () => {
  open.value = true;
};

const formState = reactive<FormState>({
  name: "",
  email: "",
  iban: "",
});
const onFinish = async (values: any) => {
  isLoading.value = true;
  await addInvestor(values);
  isLoading.value = false;
  emit("refresh-investors");
  open.value = false;
};

const onFinishFailed = (errorInfo: any) => {
  console.log("Failed:", errorInfo);
};
</script>

<template>
  <div class="flex gap-3 bg-primary shadow-lg p-4 rounded-md items-center">
    <RouterLink to="/investors">
      <a-button class="font-medium" type="text">List all Investors</a-button>
    </RouterLink>
    <RouterLink to="/bills">
      <a-button class="font-medium" type="text">List all Bills</a-button>
    </RouterLink>
    <RouterLink to="/capital-calls">
      <a-button class="font-medium" type="text">List all Capital Calls</a-button>
    </RouterLink>
  </div>
</template>

<script setup lang="ts"></script>

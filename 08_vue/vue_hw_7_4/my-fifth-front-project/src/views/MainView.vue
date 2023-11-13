<template>
  <div>
    <h2>메인 페이지</h2>
    <MainPage
      v-for="info in balances"
      :key="info.name"
      :info="info"
    />
  </div>
</template>

<script setup>
  import MainPage from '@/components/MainPage.vue'
  import { useBalanceStore } from '../stores/balance';
  const store = useBalanceStore()
  const { balances } = store
  // console.log(balances)
</script>

<style scoped>

</style>
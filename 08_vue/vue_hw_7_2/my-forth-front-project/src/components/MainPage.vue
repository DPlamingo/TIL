<template>
  <div>
    <h1>피니아 연습하기</h1>
    <ParentPage
      v-for="info in store.familyInfos"
      :key="info.familyName"
      :info="info."
    />
  </div>
</template>

<script setup>
  import ParentPage from './ParentPage.vue';
  import { useFamilyStore } from '../stores/family';
  const store = useFamilyStore() 
  // const { familyInfos } = store
  // store 변수에다가 담아준다.
  // 내가 필요한것 패밀리 인포스라하는 객체, 객체 구조분해 할당 형태로쓰거나, 
  // parent page를 v-for로 반복하던지
</script>

<style scoped>

</style>
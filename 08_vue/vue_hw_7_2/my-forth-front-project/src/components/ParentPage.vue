<template>
  <div>
    <h2>부모 컴포넌트</h2>
    <p>가문명 : {{ info.familyName }}</p>
    <p>{{ info.father }}</p>
    <p>{{ info.mother }}</p>
    <ChildPage 
      v-for="child in info.children"
      :key="child.name"
      :child="child"
    />
  </div>
</template>

<script setup>
  import ChildPage from './ChildPage.vue';
  defineProps({
    info: Object
  })
  
</script>

<style scoped>

</style>
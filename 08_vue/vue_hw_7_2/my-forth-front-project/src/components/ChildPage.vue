<template>
  <div>
    <h3>자식 컴포넌트</h3>
    <p>{{ child.name }}</p>
  </div>
</template>

<script setup>
  defineProps({
    child: Object
  })
</script>

<style scoped>

</style>
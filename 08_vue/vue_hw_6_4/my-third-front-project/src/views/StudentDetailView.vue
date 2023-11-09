<template>
  <div> 
    <!-- 페이지 잘 넘어왔네? 글면 꾸미면됨 -->
    <p>이름 : {{ name }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRoute } from 'vue-router';
const route = useRoute()
console.log(route.params)
const name = ref(route.params.name)
</script>

<style scoped>

</style>
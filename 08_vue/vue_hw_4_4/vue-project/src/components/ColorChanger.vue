<template>
  <div>
    <!-- 양방향 바인딩 colorClass -> test -> colorclass(p tag) -->
    <input type="text" v-model="colorClass">
    <p>{{ colorClass }}</p>
    <!-- 단방향 바인딩 :으로 colorClass 값을 class으로 데려온다. -->
    <p :class="colorClass">작성한 내용대로 글씨 색이 바껴야함.</p>
  </div>
</template>

<script setup>
  import { ref } from 'vue';

  const colorClass = ref('test')

</script>

<style scoped>
  .red {
    color: red;
  }
  .blue {
    color: blue;
  }
  .orange {
    color: orange;
  }
</style>
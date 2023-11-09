<script setup>
import { RouterLink, RouterView } from 'vue-router'
import MainPage from './components/MainPage.vue';


// views 안의 vue 파일은 보통 페이지가 넘어갈때 사용하는 파일들이며,
// 특별히 components안에 들어있는 것과 다른기능이 없지만 약속이다.
</script>

<template>
  <MainPage />  
  <header>
  
    <nav>
      <RouterLink :to="{ name: 'some'}">Some</RouterLink>
        |
      <RouterLink :to="{ name: 'other'}">Other</RouterLink>
        |
      <RouterLink :to="{ name: 'students'}">Students</RouterLink>


    </nav>
  </header>

  <RouterView />
</template>

<style scoped>

</style>

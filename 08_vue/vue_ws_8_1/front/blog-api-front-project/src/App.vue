<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>

    <div class="wrapper">

      <nav>
        <RouterLink :to="{name: 'main'}">Main </RouterLink>
        <RouterLink :to="{name: 'posts'}">Posts </RouterLink>

      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
.wrapper {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
}
nav {
  background-color: gray;
  padding: 1rem; 
  text-align: center;
  /* 픽셀 보다 상대단위인 rem를 사용하는 것이 좋다
  우리는 Chrome으로 desktop에서 보고있는데,  */
}
nav a {
  /* display: flex; */
  /* justify-content: center; */
  text-align: center;
  text-decoration: none;
  font-weight: bold;
}

</style>

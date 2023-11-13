<template>
  <div>
    <p>이름 : {{ info.name }}</p>
    <p>잔고 : {{ info.balance }}</p>
    <!-- <RouterLink :to="{name:'update', params:{username: info.name}}">updateBalance</RouterLink> -->
    <!-- <button>updateBalance</button> -->
    <button @click="goToUpdate">updateBalance</button>
    <!-- <button @clic></button> -->
    <hr>
  </div>
</template>

<script setup>
import { propsToAttrMap } from '@vue/shared';
import { useRouter } from 'vue-router';

defineProps({
  info: Object
})

const router = useRouter()

const goToUpdate = function () {
  router.push({
    name: 'update',
    params: {
      username: propsToAttrMap.info.name
    }
  })
}

</script>

<style scoped>

</style>
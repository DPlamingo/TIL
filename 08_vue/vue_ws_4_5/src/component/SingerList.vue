<template>
  <div>
    <h1>가수 목록</h1>
    <ul>
      <p>{{ singer }}</p>
      <SingerDetail 
        v-for="singer in singers"
        :key ='singer.name'

      />
        

    </ul>
  </div>
</template>

<script setup>
import SingerDetail from '@/component/singers/SingerDetail.vue';

const singer = [
  {
    name: '어유'
  },
  {
    name: 'adele'
  },
  {
    name: 'muse'
  },


]


</script>




<style scoped>

</style>
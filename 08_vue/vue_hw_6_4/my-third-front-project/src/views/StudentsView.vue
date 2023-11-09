<template>
  <div>
    <h1>학생 목록입니다.</h1>
    <p
      v-for="student in students"
      :key="student.name"
      @click="$event => moveToPage(student.name)"
    >
      {{ student.name }} 학생 정보 상세보기
    </p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router'
const router = useRouter()

const students = ref([
  { name: '김하나'},
  { name: '김두리'},
  { name: '김서이'},

])
const moveToPage = function(name) {
  router.push({ 
    name: 'studentDetail',
    params: {
      name: name
    } 
  }) // name이라는 이름을 어디에 담아서 보내냐
  // 인자를 가진 정보로 보냄 redirect 보내는것 처럼
  // 어딘가로 보낸방ㅂㅂ은 router link랑 똑같은 방법으로 쓰면됨
  // router lacation row
}
</script>

<style scoped>

</style>
<template>
  <div>
    <h1 v-if="route.name === 'postCreate'">게시글 생성 페이지</h1>
    <h1 v-else-if="route.name === 'postUpdate'">게시글 수정 페이지</h1>
    <!-- form 태그 -->
    <form @submit.prevent="route.name === 'postCreate'? createPost(): updatePost()">
      <!-- 선택할 카테고리 목록 -->
      <label for="category">카테고리</label>
      <select id="category" v-model="data.category">
        <option 
          v-for="category in store.categoryList"
          :key="category.id"
          :value="category.id"
        >
          {{ category.name }}
        </option>
      </select>
      <!-- 제목 -->
      <label for="title">제목</label>
      <input type="text" id="title" v-model="data.title">
      <!-- 내용 -->
      <label for="content">내용</label>
      <input type="text" id="content" v-model="data.content">
      <!-- 버튼 : 게시글 생성 -->
      <button v-if="route.name === 'postCreate'">게시글 생성</button>
      <button v-else-if="route.name === 'postUpdate'">게시글 수정</button>

    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue';
import { onMounted } from 'vue';
import { useCategoryStore } from '@/stores/category'
import { useRoute, useRouter } from 'vue-router';
import { usePostStore } from '../stores/post';
const store = useCategoryStore()
const route = useRoute()
const router = useRouter()
const postStore = usePostStore()
let post = ref({})
if (route.name === 'postUpdate') {
  post = postStore.post
}

onMounted(() => {
  store.getCategoryList()
})

const data = ref({
  title: post.title,
  content: post.content,
  category: post.category?.id
})
const createPost = function () {
  axios({
    method: 'POST',
    url: `http://127.0.0.1:8000/api/v1/posts/${route.params.pk}/`,
    data: data.value
  })
    .then(res => router.push({name: 'detail', params: {pk: res.data.id}}))
    .catch(err => console.log(err))
}

  // input 태그에 입력한 내용 담을수 있는 객체
    // 카테고리는 -> db에 있는 목록을 보여줘야 한다.
      // store에서 category 전체 목록 
      // axios 요청 보내서 응답 받은 데이터
    // submit 이벤트 발생시에는
      // 담고 있는 데이터들 모아서 
      // POST 요청 보내야 한다.
</script>

<style scoped>

</style>
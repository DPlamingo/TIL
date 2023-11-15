<template>
  <div>
    <h1>게시글 상세 조회 페이지</h1>
    <div>
      <p>id : {{ store.post.id }}</p>
      <p>category : {{ store.post.category.name }}</p>
      <p>title : {{ store.post.title }}</p>
      <p>content : {{ store.post.content }}</p>
      <p>created_at : {{ store.post.created_at }}</p>
      <p>updated_at : {{ store.post.updated_at }}</p>
    </div>
    <hr>
    <button @click="goToUpdate">게시글 수정</button>
    <button @click="goToDelete">게시글 삭제</button>
  </div>
</template>

<script setup>
  import axios from 'axios';
  import { useRoute } from 'vue-router';
  import { useRouter } from 'vue-router';
  const route = useRoute()
  const router = useRouter()
  const pk = route.params.pk
  const post = ref({})
  store.getDetailPost(pk)

  const goToDelete = function () {
    axios({
      method: 'DELETE',
      url: `http://127.0.0.1:8000/api/v1/posts/${pk}/`
    })
      .then(res => {
        console.log(res)
        router.push({name: 'posts'})
      })
      .catch(err => console.log(err))
  }
  
  const goToupdate = function () {
    router.push({name: 'postUpdate', params:{pk: pk}})
  }
</script>

<style scoped>

</style>
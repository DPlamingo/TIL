import axios from 'axios'
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const usePostStore = defineStore('post', () => {
  // 백엔드 서버에 Post 전체 목록 GET 요청.
  // axios가 필요하다 이녀석은 라이브러리다
  // axios.get(url)
  // const variable func()
  // variable.method()
  // func().method()
  const postList = ref([])
  const getPostList = function () { // 이것이 actions이다.
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/posts/'
    })
      .then(response => {
        postList.value = response.data
      }) // 성공한 경우
      .catch(error => {
        console.log(error)
      }) // 실패한 경우
    }
  return {
    getPostList, postList
  }
})

<template>
  <div>
    <h1>비디오 검색</h1>
    <!-- 기존 제품 목록 -->

    <!-- 비디오 결과 표시 -->
    <div v-if="videoResults && videoResults.length > 0" class="video-list">
      <div v-for="video in videoResults" :key="video.id.videoId" class="video-card">
        <img :src="video.snippet.thumbnails.default.url" alt="">
        <strong>{{ video.snippet.title }}</strong>
        <!-- 다른 관련 비디오 정보를 추가하세요 -->
        <button @click="goBack(product)">뒤로가기</button>
        <!-- 비디오를 장바구니에 추가하거나 다른 작업을 수행하기 위한 버튼을 추가할 수 있습니다 -->
      </div>
    </div>

    <div v-else>
      <strong>검색된 비디오가 없습니다.</strong>
    </div>
  </div>

</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const videoResults = ref([]) // 비디오 결과를 저장할 ref 변수 추가


const Search = async (product) => {
  try {
    const searchTerm = product.title; // 검색어를 요구사항에 맞게 조정하세요
    const apiKey = 'YOUR_API_KEY';
    const apiUrl = `https://www.googleapis.com/youtube/v3/search?q=${searchTerm}&key=${apiKey}&part=snippet&type=video`;

    const response = await fetch(apiUrl);
    const data = await response.json();

    // 데이터 처리 및 비디오 결과 표시
    console.log(data.items); // 이 코드는 비디오 항목을 콘솔에 기록합니다
  } catch (error) {
    console.error('YouTube API를 가져오는 중 오류 발생:', error);
  }
};


const goBack = (video) => {
  // 이전 페이지로 이동하는 로직 추가
  // router.push(...) 등을 사용하여 이동할 수 있습니다.
};

</script>

<style scoped>

</style>

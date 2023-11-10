<!-- ReviewSearch.vue -->
<template>
  <div>
    <input type="text" v-model="query" placeholder="영화 제목을 입력하세요">
    <button @click="searchReviews">검색</button>
    <div v-if="reviews.length">
      <youtube-card
        v-for="review in reviews"
        :key="review.id.videoId"
        :review="review"
        @click="openModal(review.id.videoId)"
      />
    </div>
    <youtube-modal v-if="selectedVideoId" :video-id="selectedVideoId" @close="selectedVideoId = null" />
  </div>
</template>

<script>
import axios from 'axios';
import YoutubeCard from '../components/YoutubeCard.vue';
import YoutubeModal from '../components/YoutubeModal.vue';

export default {
  components: {
    YoutubeCard,
    YoutubeModal
  },
  data() {
    return {
      query: '',
      reviews: [],
      selectedVideoId: null
    };
  },
  methods: {
    async searchReviews() {
      const YOUTUBE_API_KEY = import.meta.env.VITE_YOUTUBE_API_KEY;
      const response = await axios.get(`https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q=${this.query} 리뷰&type=video&key=${YOUTUBE_API_KEY}`);
      this.reviews = response.data.items;
    },
    openModal(videoId) {
      this.selectedVideoId = videoId;
    }
  }
};
</script>

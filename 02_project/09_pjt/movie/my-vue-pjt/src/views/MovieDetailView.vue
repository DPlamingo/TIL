<template>
  <div>
    <h1>{{ movie.title }}</h1>
    <!-- 영화 상세 정보를 표시하는 코드를 추가할 수 있습니다 -->
    <button @click="fetchTrailerId(movie.title)">유튜브 예고편 보기</button>
    <div v-if="trailerId">
      <!-- YouTube 비디오를 임베드하여 표시하는 코드를 추가할 수 있습니다. -->
      <iframe width="560" height="315" :src="`https://www.youtube.com/embed/${trailerId}`" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      movie: {},
      trailerId: null
    };
  },
  async created() {
    const movieId = this.$route.params.movieId;
    const TMDBapiKey = import.meta.env.VITE_TMDBapikey;
    const response = await fetch(`https://api.themoviedb.org/3/movie/${movieId}?api_key=${TMDBapiKey}&language=en-US`);
    this.movie = await response.json();
  },
  methods: {
    async fetchTrailerId(query) {
      const YOUTUBE_API_KEY = import.meta.env.VITE_YOUTUBE_API_KEY; // 여기에 YouTube API 키를 넣어주세요.
      const response = await fetch(`https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q=${query} Official Trailer&type=video&key=${YOUTUBE_API_KEY}`);
      const data = await response.json();

      if (data.items.length > 0) {
        this.trailerId = data.items[0].id.videoId;
      }
    }
  }
};
</script>


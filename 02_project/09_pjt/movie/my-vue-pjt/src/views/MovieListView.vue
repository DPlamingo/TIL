<template>
  <div>
    <h1>최고 평점 영화 조회</h1>

    <!-- 영화 목록 표시 -->
    <div v-if="movies && movies.length > 0" class="movie-list">
      <MovieCard v-for="movie in movies" :key="movie.id" :movie="movie" />
    </div>

    <div v-else>
      <strong>영화 목록이 없습니다.</strong>
    </div>
  </div>
</template>

<script>
import MovieCard from '../components/MovieCard.vue';
import { ref, onMounted } from 'vue';

export default {
  components: {
    MovieCard
  },
  setup() {
    const movies = ref([]);
    const TMDBapiKey = process.env.VITE_TMDBapikey; // .env 파일에서 API 키를 가져옴

    const fetchMovies = async () => {
      try {
        const apiUrl = `https://api.themoviedb.org/3/discover/movie?api_key=${TMDBapiKey}&language=en-US&sort_by=vote_average.desc&vote_count.gte=1000`;

        const response = await fetch(apiUrl);
        const data = await response.json();

        movies.value = data.results;
      } catch (error) {
        console.error('TMDB API에서 영화 데이터를 가져오는 중 오류 발생:', error);
      }
    };

    onMounted(fetchMovies);

    return {
      movies
    };
  },
};
</script>


<style scoped>
/* CSS 스타일링을 추가할 수 있습니다. */
</style>

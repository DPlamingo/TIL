
<template>
  <router-link :to="`/${movie.id}`">
    <div class="movie-card">
      <img :src="getImageUrl(movie.poster_path)" alt="">
      <div class="movie-info">
        <strong>{{ movie.title }}</strong>
        <p>{{ movie.release_date }}</p>
        <p>평점: {{ movie.vote_average }}</p>
        <p>{{ movie.overview }}</p>
        <button @click.stop="openYoutubeModal">유튜브 예고편 보기</button> <!-- 유튜브 버튼 추가 -->
      </div>
    </div>
  </router-link>
</template>

<script>
  export default {
    props: {
      movie: {
        type: Object,
        required: true
      }
    },
    methods: {
      getImageUrl(posterPath) {
        if (posterPath) {
          return `https://image.tmdb.org/t/p/w500/${posterPath}`;
        }
        return 'https://via.placeholder.com/500';
      },
      openYoutubeModal(e) {
        e.preventDefault();
        this.$emit('openYoutube', this.movie.title); // 'openYoutube' 이벤트를 발생시킴
      }
    }
  };
</script>

<style scoped>
.movie-card {
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 500px;
  margin: auto;
}

.movie-info {
  padding: 10px;
}
@media (max-width: 600px) {
  .movie-card {
    width: 100%;
  }
}
</style>

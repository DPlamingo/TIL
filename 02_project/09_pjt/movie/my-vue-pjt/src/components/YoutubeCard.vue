<!-- YoutubeCard.vue -->
<template>
  <div class="youtube-card" @click="$emit('click', review.id.videoId)">
    <img :src="review.snippet.thumbnails.default.url" alt="">
    <h3>{{ review.snippet.title }}</h3>
  </div>
</template>

<script>
  export default {
    props: {
      review: {
        type: Object,
        required: true
      }
    }
  };
</script>

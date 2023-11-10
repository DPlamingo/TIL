<!-- YoutubeModal.vue -->
<template>
  <div class="youtube-modal" @click="close">
    <iframe width="560" height="315" :src="`https://www.youtube.com/embed/${videoId}?autoplay=1`" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  </div>
</template>

<script>
  export default {
    props: {
      videoId: {
        type: String,
        required: true
      }
    },
    methods: {
      close() {
        this.$emit('close');
      }
    }
  };
</script>

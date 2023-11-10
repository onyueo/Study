<template>
  <div>
    <h1>
      제목 : {{ video[0].snippet.title }}
    </h1>
    <p>업로드 날짜 : {{ video[0].snippet.publishedAt }}</p>
    <iframe id="player" type="text/html" width="640" height="360" :src="viewerURL" frameborder="0"></iframe>
    <p>{{ video[0].snippet.description }}</p>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { ref } from 'vue';
import axios from 'axios';

const APIKEY = import.meta.env.VITE_YOUTUBE_API_KEY;
const route = useRoute();
const video = ref('');
const videoId = route.params.videoId
console.log(route.params,'params')
console.log(videoId)
// 오자마자 정보를 가져와야 합니다.
const viewerURL = `https://www.youtube.com/embed/${videoId}`;
const YoutubeURL = `https://www.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&id=${videoId}&key=${APIKEY}`
console.log(YoutubeURL,'URL')
axios.get(YoutubeURL)
.then((response) => {
  video.value = response.data.items
  console.log(response,'response')
  console.log(video.value,'videos')
})
.catch((error)=> console.log(error,'에러러러러러러러러러러러러러러러러러러러러'))


</script>

<style  scoped>

</style>
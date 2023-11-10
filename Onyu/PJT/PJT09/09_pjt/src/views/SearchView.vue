<template>
  <h1>
    비디오 검색
  </h1>
  <div class="input-group mb-3" >
      <input class="form-control" type="text" v-model="UserInput">
      <button class="btn btn-outline-primary " @click.prevent="goSearch" >검색</button>
  </div>

  <div v-for="video in videos" :key="video.id.videoId" class='video-container' @click="goDetail(video)">

    <div class="video-img" ><img :src="video.snippet.thumbnails.medium.url" alt="" @click="goDetail(video)"></div>
    <div class="video-desc">
      {{ video.snippet.title }}
      {{ video.channelTitle }}
      {{ video.publishTime }}
    </div>
    <hr>
  </div>
  <!-- </div> -->
</template>

<script setup>
import { ref, computed } from 'vue'
import { routerKey, useRouter } from 'vue-router';
import axios from 'axios'
const UserInput = ref('')
const APIKEY = import.meta.env.VITE_YOUTUBE_API_KEY
const router = useRouter()
const videos = ref([])

// funcs
const IsVideoEmpty = computed(() => {
  console.log(videos)
  return videos.value.length > 0 ? true : false
  })

// 검색 함수
const goSearch = function (input) {
  // 입력한 값을 가져온다 -> 굳이?
  console.log(UserInput.value) // 잘 들어오는 중
  // 해당 값을 가지고 검색을 실행한다. <- API로 검색
  // console.log(input)
  // 값을 검색하기 위한 URL 을 설정해준다.
  const YoutubeURL = `https://www.googleapis.com/youtube/v3/search?key=${APIKEY}&part=snippet&type=video&q=${UserInput.value}`
  // axios 를 가져온다. > 함수를 실행시켜, 검색을 하기 위함
  console.log(YoutubeURL,'URL')
  axios.get(YoutubeURL)
  .then((response) => {
    videos.value = response.data.items
    UserInput.value = ''
    console.log(response,'response')
    console.log(videos.value,'videos')
  })
  .catch((error)=> console.log(error))
  // 검색한 목록의 동영상에 해당하는 Comp를 뿌려준다.
}

// Detail 함수
const goDetail = (video) => {
  router.push(`/detail/${video.id.videoId}`)
} 


</script>

<style  scoped>
input {
  width: 4rem;
}
.search {
  width: 200px;
}

.video-container {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.video-img {
  width: 320px;
  height: 180px;
}

.video-desc {
  text-align: center;
}
</style>
<template>
  <div>
    <h1> App.Vue </h1>
    <MyComponent />
    <MyComponent />
 
  </div>
</template>

<script setup>
import MyComponent from './components/MyComponent.vue'
// @ : /src/ 절대경로 vue에서 미리 잡아둠
import MyComponent from '@/components/MyComponent.vue'

</script>

<style scoped>

</style>
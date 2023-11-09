<template>
  <header>
    <MainPage />
      <nav>
        <RouterLink :to="{ name:'some'}">Some</RouterLink>
        <span> | </span>
        <RouterLink :to="{ name:'other'}">About</RouterLink>
        <span> | </span>
        <RouterLink :to="{ name:'students'}">Students</RouterLink>

      </nav>
  </header>


  <RouterView />
</template>

<script setup>
  import { RouterLink, RouterView } from 'vue-router'
  import MainPage from './components/MainPage.vue';


</script>

<style scoped>

</style>

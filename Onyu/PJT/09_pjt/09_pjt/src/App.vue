<template>
  <header></header>
  <nav>
   <RouterLink :to="{name: 'home'}">Home</RouterLink> |
   <RouterLink :to="{name: 'saved'}">saved</RouterLink> |
   <RouterLink :to="{name: 'search'}">search</RouterLink> |
   <!-- <RouterLink :to="{name: 'detail'}">detail</RouterLink> | -->

  </nav>
  <main>
    <div>
      <RouterView/>
    </div>
  </main>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';

</script>

<style  scoped>

</style>
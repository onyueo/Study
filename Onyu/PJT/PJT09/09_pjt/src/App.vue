<template>
  <header class="m-3 ">
    <nav>
      <ul class="nav nav-pills ">
        <li class="nav-item">
          <RouterLink :to="{name: 'home'}" class="nav-link" aria-current="page" href="#">Home</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{name: 'saved'}" class="nav-link" href="#" >saved</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{name: 'search'}" class="nav-link active" href="#">search</RouterLink>
        </li>
      </ul>
    </nav>
  </header>

  <main class="m-3">
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
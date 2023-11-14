<template>
  <div>
    <h1>Todo PJT</h1>
    <h2>완료된 todo : {{ store.doneTodosCount }}</h2>
    <TodoForm />
    <TodoList />
  </div>
</template>

<script setup>
// store
import { useCounterStore } from '@/stores/counter';

import TodoForm from '@/components/TodoForm.vue';
import TodoList from '@/components/TodoList.vue';

const store = useCounterStore()


</script>

<style scoped>

</style>

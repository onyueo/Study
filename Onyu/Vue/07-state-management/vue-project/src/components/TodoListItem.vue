<template>
  <div>
    <span>할일 : </span>
    <span 
      @click="store.updateTodo(todoData.id)"
      :class="{'is-done': todoData.isDone}"
      >
      {{ todoData.text }}
    </span>
    <button @click="store.deleteTodo(todoData.id)">삭제</button>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore()

defineProps({
  todoData: Object
})

</script>

<style  scoped>
.is-done {
  text-decoration: line-through;
}
</style>
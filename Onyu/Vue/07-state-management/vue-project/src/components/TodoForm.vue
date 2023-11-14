<template>
  <div>
    <form @submit.prevent="createTodo()" ref="formElem">
      <input type="text" v-model="todoText">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter';
import { ref } from 'vue'

const todoText = ref('')
const store = useCounterStore()

// ref로 DOM요소 직접적으로 선택가능!
const formElem = ref(null)

const createTodo = function () {
  store.addTodo(todoText.value)
  // todoText.value = ''  // 혹은
  formElem.value.reset()

}


// <form @submit.prevent="createTodo(todoText)">
// 
// const createTodo = function (todoText) {
//   store.addTodo(todoText)
//   todoText.value = ''
// }

</script>

<style scoped>

</style>
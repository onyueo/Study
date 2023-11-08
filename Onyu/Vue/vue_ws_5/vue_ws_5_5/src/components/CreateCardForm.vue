<template>
  <div>
    <form action="">
      <span>이름 </span>
      <input type="text" id="name" v-model="name">
      <span>  직함 </span>
      <input type="text" id="title" v-model="title">
      <button @click.prevent="createCardFunction">명함 추가</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const emit = defineEmits(['createCardEvent'])

const name = ref('')
const title = ref('')

const createCardFunction = function() {
  const cardInfo = {name: name.value, title: title.value}
 
  // console.log(cardInfo.value)
  emit('createCardEvent', cardInfo)
  name.value=''
  title.value=''
}
</script>

<style scoped>
#name, #title {
  height: 30px;
  border-radius: 5px;
  border-color: rgb(36, 139, 180);
}

button {
  margin-left: 15px;
  background-color: transparent;
  padding: 7px;
  border-radius: 5px;
  
}
</style>
<template>
  <div>
    <ParentChild 
      my-msg="msg" 
      :dynamic-props="name"
      @some-event="someCallback"
      @emit-args="getNumvers"
      @updateName22="updateName33"
    />
    
  </div>
</template>

<script setup>
import ParentChild from '@/components/ParentChild.vue';

import { ref } from 'vue'

const name = ref('Alice')
const someCallback = function () {
  console.log('자식이 보낸 emit이벤트 수신!')
}

const getNumvers = function(...args) {
  // 배열로 return 
  console.log(args)
}

const updateName33 = function() {
  name.value = 'Bella'
}

</script>

<style scoped>

</style>
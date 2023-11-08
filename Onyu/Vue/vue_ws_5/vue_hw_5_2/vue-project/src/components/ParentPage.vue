<template>
  <div>
    <h1>부모 페이지 입니다.</h1>
    <div v-for="childs in children">
      <ChildPage 
        :child="childs"
        @give-me-allowance="updateBalance(childs)"
      />
    </div>

  </div>
</template>


<script setup>
import ChildPage from '@/components/ChildPage.vue';
import { ref } from 'vue'

const children = ref([
  {name: '김하나', age: 30, balance: 100000},
  {name: '김두리', age: 20, balance: 10000},
  {name: '김서이', age: 10, balance: 1000}
])

const updateBalance = function(child) {
  // console.log(child.balance)
  child.balance += 1000
}

</script>


<style  scoped>

</style>
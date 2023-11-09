<template>
  <div>
    
    <nav>
      <p></p>
      <RouterLink v-for="student in students" :to="{ name: 'studentdetail', params: {name: student.name} }">
        {{ student.name }} 학생 정보 보기
        <p></p>
      </RouterLink>
    </nav>

  </div>
</template>


<script setup>
import { ref } from 'vue'


const students = ref([
  {name: '김하나'},
  {name: '김두리'},
  {name: '김서이'}
])


</script>

<style scoped>

</style>
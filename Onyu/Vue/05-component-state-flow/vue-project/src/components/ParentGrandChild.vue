<template>
  <div>
    {{ myMsg }}
    <button @click="updateName11">이름 변경!!</button>
  </div>
</template>

<script setup>
defineProps({
  myMsg: String,

})

// 부모에게 이름 변경 요청 실습
const emit = defineEmits(['updateName'])

const updateName11 = function () {
  emit('updateName')
}
</script>

<style scoped>

</style>
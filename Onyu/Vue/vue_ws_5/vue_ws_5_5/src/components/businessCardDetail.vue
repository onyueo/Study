<template>

  <div class="card">
    <h3>이름 : {{ bcard.name }}</h3>
    <p>직함 : {{ bcard.title }}</p>
    <button @click="deleteCardFunc">명함 삭제</button>
  </div>

</template>

<script setup>
  const props = defineProps({
    bcard: Object
  })

  const emit = defineEmits(['deleteCardEvent'])
  const deleteCardFunc = function () {
    // console.log(props.bcard)
    emit('deleteCardEvent')
  }
</script>

<style scoped>

.card {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: whitesmoke;
  width: 40%;
  padding: 20px;
  margin: 10px;
  border: 1px solid lightgrey;
}

h3 {
  margin-bottom: 0px;
}
</style>
<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
    <!-- <ParentGrandChild my-msg="msg"/> -->
    <ParentGrandChild 
      :my-msg="myMsg"
      @update-name="updateName22"
      />
    <button @click="$emit('someEvent')"> 클릭 </button>

    <button @click="buttonClick"> 클릭 </button>

    <button @click="emitArgs"> 추가인자 전달 </button>
    
  </div>
</template>

<script setup>

import ParentGrandChild from '@/components/ParentGrandChild.vue'


const props = defineProps({
  myMsg: String,
  dynamicProps: String,
  // 유효성검증 -> value = msg(myMsg) 가 []안에 있으면 ok, 없으면 wornig

  // 예시1
  // vaildator(value) {
  //   return ['a', 'b', 'c'].includes(value)
  // }

  // 예시22
  vaildator(value) {
    const valdValues = ['a', 'b', 'c']
    if (!valdValues.includes(value)) {
      console.error('에러입니다.')
      return false
    }
    return true
  }
})

console.log(props)
console.log(props.myMsg)


// emit 선언 방식

const emit = defineEmits(['someEvent', 'emitArgs', 'updateName11'])

const buttonClick = function() { 
  emit('someEvent') 
}

const emitArgs = function() {
  emit('emitArgs', 1, 2, 3)
}

const updateName22 = function () {
  emit('updateName11')
}

</script>

<style scoped>

</style>
<template>
  <div>
    <header>
      <div>명함 관리 페이지</div>
    </header>

    <main>
      <p>명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
      <CreateCardForm 
        @create-card-event="updateCard"
      />
  
      <BusinessCard 
        :new-card="newCard"
      />
    </main>

    <footer><p>🐣 2023 My Business Cards</p></footer>
  </div>
</template>

<script setup>
import BusinessCard from '@/components/BusinessCard.vue';
import CreateCardForm from '@/components/CreateCardForm.vue';
import { ref } from 'vue'

const newCard = ref(null)
const updateCard = function(cardInfo) {
  // console.log(cardInfo)
  // console.log(cardInfo[0]['name'])
  newCard.value = cardInfo
}

</script>

<style scoped>
header{
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgb(0, 122, 204);
  color: white;
  font-size: 30px;
  width: 400px;
  height: 100px;
  margin: auto;

}

main{
  text-align: center;
  margin-bottom: 50px;
}

footer{
  text-align: center;
  width: 100%;
  bottom : 0;
  position : fixed;
  background-color: lightgray;
}

</style>
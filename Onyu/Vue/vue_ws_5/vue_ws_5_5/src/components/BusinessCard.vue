<template>
  <div>
    <h2>보유 명함 목록</h2>
    <!-- <p v-show="businessCards.length">보유중인 명함 수 : {{ businessCards.length }}</p>
    <p v-show="!businessCards.length">명함이 없습니다. 새로운 명함을 추가해 주세요.</p> -->
    <p>{{ restCards }}</p>

    <div class="cards">
      <BusinessCardDetail 
        v-for="businessCard in businessCards"
        :bcard="businessCard"
        @delete-card-event="deleteCard(businessCard)"
      />
    </div>
    
  </div>
</template>

<script setup>
import BusinessCardDetail from '@/components/businessCardDetail.vue';
import { ref, computed, watch } from 'vue'


const businessCards = ref([
  {name: '일론머스크', title:'테슬라 테크노킹'},
  {name: '래리 엘리슨', title: '오라클 창업주'},
  {name: '빌 게이츠', title: '마이크로소프트 공동창업주'},
  {name: '래리 페이지', title: '구글 공동창업주'},
  {name: '세르게이 브린', title: '구글 공동창업주'},
])

const deleteCard = function(event) {
  businessCards.value = businessCards.value.filter((test) => {
    return event !== test
  })
}

const restCards = computed(() => {
  return businessCards.value.length > 0 ? 
  `보유중인 명함 수 : ${businessCards.value.length}`: '명함이 없습니다. 새로운 명함을 추가해 주세요.'
})

const props = defineProps ({
  newCard: Object
})

watch(() => props.newCard, (card) => businessCards.value.push(card))

</script>

<style scoped>
.cards{
  display: flex;
  text-align: center;
  justify-content: space-evenly;
  align-items: space-between;
  flex-wrap: wrap;
}
</style>
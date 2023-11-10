<template>
  <div>
    <h1>상품 디테일</h1>
    <div v-if="product" class="product-card">
      <img :src="product.image" alt="">
      <strong>{{ product.title }}</strong>
      <p>가격 : ${{ product.price }}</p>
      <button @click="goDetail(product)">상세페이지로 이동</button>
      <button @click="addCart(product)">장바구니에 추가</button>
    </div>
    <div v-else>
      <strong>로딩중입니다...</strong>
    </div>
  </div>

</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router';
import axios from 'axios'

// 넘겨준 데이터 받야야함? -> uesRoute
const route = useRoute()
const product = ref('')
const productId = route.params.productId
const storeURL = `https://fakestoreapi.com/products/${productId}`


axios.get(storeURL)
  .then((response) => {
    // console.log(response.data)
    product.value = response.data
  }).catch((error) => {
    console.log(error)
  })

</script>

<style scoped>

</style>
<template>
  <div>
    <h1>메인페이지</h1>
    <!-- <div v-if="products"> 안됨! -->
    <!-- <div v-if="products.length > 0"> 여기에 넣지 않도록 주의! -> computed 쓰기-->
    <div v-if="productIsEmpty" class="product-list">
      <div v-for="product in products" :key="product.id" class="product-card">
        <!-- {{ product }} -->
        <img :src="product.image" alt="">
        <strong>{{ product.title }}</strong>
        <p>가격 : ${{ product.price }}</p>
        <button @click="goDetail(product)">상세페이지로 이동</button>
        <button @click="addCart(product)">장바구니에 추가</button>
      </div>
    </div>
    <div v-else>
      <strong>로딩중이거나, 상품 정보가 없습니다.</strong>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router';
import axios from 'axios'

// 클릭하면 이동해야하네? -> useRouter

const router = useRouter()
const products = ref([])
const storeURL = 'https://fakestoreapi.com/products'

axios.get(storeURL)
  .then((response) => {
    // console.log(response.data)
    products.value = response.data
  }).catch((error) => {
    console.log(error)
  })

const productIsEmpty = computed (() => {
  // return products.length > 0 ? true : false   ## value 주의!!
  return products.value.length > 0 ? true : false
})


const goDetail = (product) => {
  // id 값도 같이 주어야 하니까 url수정!
  router.push(`/${product.id}`)
}


// 추가할때마다 기존에 있던 데이터에 저장해놓아야함!
// 임시로 저장할 공간필요, 브라우저 스토리지 있음 - local Storage
// 반영구적으로 저장할 수 있는 공간 (브라우저를 껐다 켜도 데이터 유지됨)
// 5mb정도의 데이터 저장 가능 // 쿠키보다 많은 데이터 저장가능
// 하지만, 보안이 조금 위험함 -> 위험수준이 낮은 데이터만 저장해야함!!
const addCart = (product) => {
  // 주의!! value에는 '문자열' 만 사용가능!! 
  // JSON형식으로 쓰려면-> 문자열로 변환해야함 (get은 반대)

  // 하나의 데이터만 저장됨 -> 문제점 : 덮어쓰기 된다
  // localStorage.setItem('cart', JSON.stringify(product))

  // 데이터 가져오기
  // const temp = localStorage.getItem('cart')
  // console.log(temp)

  // 여러 데이터 저장하기
  // 현재 local storage에 저장된 데이터 가져오고 없다면 빈리스트로 초기화
  const existingCart = JSON.parse(localStorage.getItem('cart')) || []
  // 중복 아니면 추가 (빈리스트 일때 주의-existingCart.length > 0 &&)
  const isDuplicate = existingCart.length > 0 && existingCart.find((item) => item.id === product.id)

  if(!isDuplicate) {
    alert('장바구니에 추가합니다')
    existingCart.push(product)
  } else {
    alert('이미 있는 상품입니다. 장바구니로 이동합니다')
  }

  // 수정된 카트 데이터를 localStorage에 저장
  localStorage.setItem('cart', JSON.stringify(existingCart))

  router.push('/cart')

}

</script>

<style scoped>



</style>

<!-- 공통으로 CSS적용해야할 때  -->

<style>

.product-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.product-card {
  border: 1px solid black;
  width: 220px;
}

.product-card img {
  width: 200px;
  height: 230px;
  object-fit: fill;
}
</style>
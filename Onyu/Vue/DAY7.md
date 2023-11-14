# 11.13 (월)

## State Management (상태관리)
Vue컴포넌트는 이미 반응형 상태를 관리하고 있음 ( 상태 === 데이터 )

컴포넌트 구조의 단순화

상태 -> 뷰 -> 기능 -> 상태 .....

이러한 사이클을 가져감 (단방향 데이터 흐름)


### 상태 관리의 단순성이 무너지는 시점

> 여러 컴포넌트가 동일한 상태를 공유할 때!
>  1. 여러 뷰가 동일한 상태에 종속되는 경우
>  2. 서로 다른 뷰의 기능이 동일한 상태를 변경시키는 경우


1. 여러 뷰가 동일한 상태에 종속되는 경우
   - 공유상태를 공통조상 컴포넌트로 끌어올린 다음 props로 전달하는 것
   - 하지만, 계층구조가 깊어질경우 비효율적, 관리가 어려워짐

2. 서로 다른 뷰의 기능이 동일한 상태를 변경시키는 경우
   - 발신(emit)된 이벤트를 통해 상태의 여러 복사본을 변경 및 동기화 하는 것
   - 마찬가지로 관리의 패턴이 깨지기 쉽고 유지 관리할 수 없는 코드가 됨


### 해결책!
- 각 컴포넌트의 공유상태를 추출하여 전역에서 참조할 수 있는 저장소에서 관리
  - 별도로 전역적으로 참조할 수 있는 중앙 저장소에 저장
  - 의존성 생각할 필요 없음!, 실시간 동기화 가능!

- Pinia (피냐!)를 Statemanagement 활용
  - Vue의 공식 상태 관리 라이브러리!
  - 모든 컴포넌트가 트리계층 구조에 관계없이 상태에 접근하거나 기능을 사용할 수 있음


## Pinia (State management library)
  Vue의 공식 상태 관리 라이브러리!

- vite 프로젝트 빌드 시 pinia 라이브러리 간편하게 추가할 수 있음

> ### Pinia 구성 요소
> 1. store
> 2. state
> 3. getters
> 4. actions
> 5. plugin
>

### Store (counter.js)
- 중앙저장소
- 모든 컴포넌트가 공유하는 상태, 기능 등이 작성됨
- defindStore을 통해서 만들어짐!
- 만약 store에 state를 정의하지 않았다면 컴포넌트에서 새로 추가할 수 있음
- 

피냐에서는 data를 상태라고 부름!
- ref() === state
  
계산된 값!
- computed() === getters

메서드! 
- function() === actions

plugin
- 어플리케이션의 상태관리에 필요한 추가 기능을 제공하거나 확장하는 도구나 모듈
- 패키지 매니저 설치 이후 별도 설정을 통해 추가됨


```
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
// 피냐의 중앙저장소!!

export const useCounterStore = defineStore('counter', () => {
  // 상태
  const count = ref(100)
  const doubleCount = computed(() => count.value * 2)


  // 기능
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
})


--------------

<template>
  <div>
    <p>{{ store.count }}</p>
    <p>{{ newNumber }}</p>

    <p>{{ store.doubleCount }}</p>

    <button @click="store.incresement()">버튼</button>
  </div>
</template>

<script setup>
// store
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore()

console.log(store.count)

const newNumber = store.count + 1

// store.count = 100
// 중앙저장소에서도 값이 바뀜 -> but 위험! 값을 바꾸면 안됨
// -> getters(computed) or actions(functions)을 이용해서 간접적으로 상태 바꾸어야함


// Getters
console.log(store.doubleCount)

// Actions
// getters와 달리 state조작, 비동기, API호출이나 다른 로직을 진행할 수 있음


</script>

```


### Pinia 실습! - Todo!

npm i pinia-plugin-persistedstate
# 11.06 (월)


## Computed Properties

### Computed()
계산된 속성을 정의하는 함수

미리 계산된 속성을 사용하여 템플릿에서 표현식을 단순하게 하고 불필요한 반복연산을 줄임

``` <p>{{ todos.length > 0 ? '아직 남았다' : '퇴근'}}</p> ```

와 같은 코드에서 length를 여러번 사용하는 경우 반복이 발생 -> 미리 계산된 속성값 사용하기!

-> const { createApp, ref, computed } = Vue   (computed 추가)

```
  <p>{{ restOfTodos }}</p>

  const todos = ref([
          { text: 'Vue 실습' },
          { text: '자격증 공부' },
          { text: 'TIL 작성' }
        ])

  const restOfTodos = computed (() => {
    return todos.value.length > 0 ? '아직 남았다' : '퇴근'
  })
```

- Computed 특징
  - 반환되는 값은 computed ref이며 일반 refs와 유사하게 계산된 결과를 .value로 참조할 수 있음 (템플릿에서는 .value 생략가능)
  - computed 속성은 의존된 반응형 데이테를 **자동으로 추적**
  - 의존하는 데이터가 **변경될 때만 재평가**
    - restOfTodos의 계산은 todos에 의존하고 있음
    - 따라서 todos가 변경될 때만 restOfTodos가 업데이트 됨

- Computed 대신 method로 동일한 로직 처리 가능!
- 차이점 :
  - computed속성은 의존된 반응형 데이터를 기반으로 캐시(cached) 된다
  - 의존하는 데이터가 변경된 경우에만 재평가됨
  - 즉, 의존된 반응형데이터가 변경되지 않는 한 이미 계산된 결과에 대한 여러 참조는 다시 평가할 필요 없이 이전에 계산된 결과를 즉시 반환
  - 반면, method 호출은 다시 렌더링이 발생할 때마다 항상 함수를 실행 
  - 여러곳에서 사용되면 하나의 렌더링이 발생할 때마다 다시 실행


- #### Computed 와 method의 적절한 사용처
  - Computed  (의존된 데이터가 변경되면 자동으로 업데이트)
    - 의존하는 데이터에 따라 결과가 바뀌는 계산된 속성을 만들 때 유용
    - 동일한 의존성을 가진 여러 곳에서 사용할 때 계산 결과를 캐싱하여 중복계산 방지
  
  - method  (호출해야만 실행됨)
    - 단순히 특정 동작을 수행하는 함수를 정의할 때 사용
    - 데이터에 의존하는 지 여부와 관계없이 항상 동일한 결과를 반환하는 함수



### Cache(캐시)

데이터나 결과를 일시적으로 저장해두는 임시 저장소

이후에 같은 데이터나 결과를 다시 계산하지 않고 빠르게 접근할 수 있도록 함

- 웹 페이지의 캐시 데이터
  - 페이지의 일부 데이터를 브라우저 캐시에 저장 후 같은 페이지에 다시 요청 시 모든 데이터를 응답 받는 것이 아닌 캐시된 데이터를 사용 -> 더 빠르게 웹페이지 렌더링 가능!! (이미지 같은 것들..)



----

### v-if
표현식 값의 T/F를 기반으로 요소를 조건부로 렌더링

v-if 는 directive이기 때문에 단일 요소에만 연결 가능

이 경우 template요소에 v-if를 사용하여 하나 이상의 요소에 대해 적용할 수 있음 (v-else, v-else-if 모두 적용 가능)


- template element
  - 페이지가 로드될 때 렌더링 되지는 않지만 JS를 사용하여 나중에 문서에서 사용할 수 있도록 하는 html을 보유하기 위한 메커니증
  - 보이지 않는 wrqpper 역할


```
  <!-- if else -->
  <p v-if="isSeen">true일때 보여요</p>
  <p v-else >false일때 보여요</p>
  <button @click="isSeen = !isSeen">토글</button>

  <!-- else if -->
  <div v-if="nema === 'Alice'">Alice입니다</div>
  <div v-else-if="name === 'Bella'">Bella입니다</div>
  <div v-else-if="name === 'Cathy'">Cathy입니다</div>
  <div v-else>아무도 아닙니다.</div>

  <!-- v-if on <template> -->
  <template v-if="nema === 'Cathy'">
    <div>Cathy입니다</div>
    <div>나이는 30살입니다</div>
  </template>

```





### v-show
표현식 값의 T/F를 기반으로 요소의 가시성을 전환

v-show요소는 일단 렌더링을 함!(DOM에 남아있음) -> 이후 display 속성값으로 보여질지 말지 정함
```
  <!-- v-show -->
  <div v-show="isShow">v-show</div>
  <div style="display: none;">v-show</div>
```




### v-if VS v-show

v-if
  - 초기 조건이 false인 경우 아무 작업도 수행하지 않음
  - 토글 비용이 높음 (지우고 새로 렌더링 해야하기 때문!)

v-show
  - 초기 조건에 관계없이 항상 렌더링 (초기렌더링 비쌈 // 토글은 쉬움)
  - 초기 렌더링 비용이 더 높음

=> 무언가를 매우 자주 전환해야 하는 경우 v-show를, 실행중 조건이 변경되지 않는 경우에는 v-if 권장!!





## List Rendering ( 반복 )


### v-for
소스데이터를 기반으로 요소 또는 템플릿 블록을 여러 번 렌더링

alias in expression 형식의 특수구문을 사용하여 반복되는 요소에 대한 별칭(alias)을 제공

인덱스(객체에서는 키) 에 대한 별칭을 지정할 수 있음 
  - 두개 출력시 : 첫번째는 값,두번째는 index
  - 세개 출력시 : 첫번째는 값, 두번째는 key, 세번째는 index

```
  <div v-for="(item, index) in myArr">
    {{ index }} // {{ item }}
    {{ item.name }}
  </div>

  <div v-for="(value, key, index) in myObj">
    {{ index }} / {{ key }} / {{ value }}
  </div>



  <!-- v-for on <template> 포장지-->
  <ul>
    <template v-for="item in myArr">
      <li> {{ item.name }} </li>
      <li> {{ item.age }} </li>
      <hr>
    </template>
  </ul>

  
  <!-- nested v-for 중첩 가능-->
  <ul v-for="item in myInfo">
    <li v-for="friend in item.friends">
      {{ friend }}
    </li>
  </ul>

```

### v-for with key
## 약속 1 )반드시 v-for 와 key를 함께 사용한다!!!

내부 컴포넌트 상태를 일관되게 유지 -> 데이터를 예측 가능한 행동을 유지 ( Vue 내부 동작 관련 )

- key 는 반드시 각 요소에 대한 고유값을 나타낼 수 있는 식별자여야 함 (ex-id)
  - => <div v-for="item in items" :key="item.id">

- index를 id로 쓸 수 있을까?
  - => index가 고유한 값이라고 할 수 있을까?
  - 요소가 사라져도 인덱스도 같이 사라지지 않고 유지되기때문에 안됨!


## 약속 2 ) 동일 요소에 v-for와 v-if를 함께 사용하지 않는다!
=> 동일한 요소에서 v-if가 v-for보다 우선순위가 더 높기 때문!

v-if조건은 v-for 범위의 변수에 접근할 수 없음

해결방법
1. todo 데이터 중 이미 처리한 (isComplete === true) todo만 출력하기
  - computed를 활용해 필터링 된 목록을 반환하여 반복하도록 설정

2. v-if와 v-for을 나누어 사용 - template 이용

```
  <div id="app">
    <!-- [Bad] v-for with v-if -->
    <ul v-for="todo in todos" v-if="!todo.isComplete" :key="todo.id">
      <li>
        <!-- 아무것도 안나옴! v-if="!todo = undefined -->
        {{ todo.name }} 
      </li>
    </ul>

    <!-- [Good]1 v-for with v-if & computed-->
    <ul>
      <li v-for="todo in completeTodos" :key="todo.id">
        {{ todo.name }}
      </li>
    </ul>

    <!-- [Good]2 v-for with v-if & template-->
    <ul>
      <template v-for="todo in todos" :key="todo.id">
        <li v-if="!todo.isComplete" >
          {{ todo.name }}
        </li>
      </template>
    </ul>
```


## Watch()
반응형데이터를 감시하고, 감시하는 데이터가 변경되면 콜백함수를 호출!

(Computed랑 비슷함! but 목적은 다름)

- watch 구조 
  - watch(variable, (newValue, oldValue ) => {  })
  - variable : 감시하는 변수
  - newValue : 감시하는 변수가 변화된 값, 콜백함수의 첫번째 인자
  - oldValue : 콜백함수의 두번째 인자

- return에 적어주지 않아도 됨 => 위 template에 사용하지 않고 바로 호출되는 함수이기 때문
  
```
  const countWatch = watch(count,  (newValue, oldValue) => {
    console.log(`oldValue: ${newValue}, oldValue: ${oldValue}`)
  })

  const messageWatch = watch(message, (newValue, oldValue) => {
    messageLength.value = newValue.length
  })
```

|   | computed | watchers |
|---|----------|----------|
|공통점| 데이터의 변화를 감지하고 처리, 의존/감시 하는 원본데이터 직접 변경 X|
|동작| 의존하는 데이터 속성의 계산된 값을 반환| 특정 데이터 속성의 변화를 감시하고 수행|
|사용목적| 템플릿 내에서 사용되는 데이터 연산용| 데이터 변경에 따른 특정 작업 처리용|
|사용예시| 연산된 길이, 필터링 된 목록 계산 | 비동기 API요청, 연관 데이터 업데이트 등|




## Lifecycle Hooks
Vue인스턴스의 생애주기 동안 특정 시점에 실행되는 함수

개발자가 특정 단계에서 의도하는 로직이 실행될 수 있도록 함!

1. Vue컴포넌트 인스턴스가 초기 렌더링 및 DOM요소 생성이 완료된 후 특정 로직을 수행하기
2. 반응형 테이터의 변경으로 인해 컴포넌트의 DOM이 업데이트 된 후 특정로직을 수행하기

```
  onMounted(() => {
    console.log('Mounted')
  }) // app 이 template에 연결되었을 때 자동으로 나옴

  onUpdated(() => {
    message.value = 'updated~!'
  }) // message가 변경사항이 생겼을 때 나옴
```

특징
  - Vue는 Lifecycle Hooks에 등록된 콜백함수들을 인스턴스와 자동으로 연결함
  - 이렇게 동작하려면 hooks 함수들은 반드시 동기적으로 작성되어야 함
  - 인스턴스 생애 주기의 여러 단계에서 호출되는 다른 hooks도 있으며 일반적으로 onMounted, onUpdated, onUnMounted



### Vue Style Guide
우선순위에따라 4가지 범주로 나눔
- A : 필수 (Essential) - 오류를 방지하는데 도움이 되므로 어떤 경우에도 규칙을 학습하고 준수
  - v-for 에 key사용하기
  - v-if와 v-for를 같이 사용하지 않기
- B : 적극권장 (Strongly Recommended)
- C : 권장 (Recommended)
- D : 주의 필요 (Use with Caution)


#### 주의! - Computed의 반환 값은 변경하지 말 것
- computed의 반환 값은 의존하는 데이터의 파생된 값
- 일종의 snapshot이며 의존하는 데이터가 변경될 때 마다 새 snapshot이 생성됨
- snapshot을 변경하는 것은 의미가 없으므로 계산된 반환 값은 읽기 전용으로 취급되어야 하며 변경되어서는 안됨
- 대신 새 값을 얻기 위해서는 의존하는 데이터를 업데이트 해야 함
- reverse() 나 sort()는 원본배열을 변경하기 때문에 복사본을 만들어 진행해야함
  - num.reverse() X,  [...num].reverse() O


- 수정 매서드 (원본 배열수정)
  - Vue는 반응형 배열의 변경 메소드가 호출되는 것을 감지하여, 필요한 업데이트를 발생시킴
  - push, pop, shift, unshift, splice, sort, reverse
  
- 배열 교체
  - 원본배열을 수정하지 않고 항상 새 배열을 반환
  - filter, concat, slice
# 11.02 (목)

> ## Template Syntax
> : DOM을 기본 구성 요소 인스턴스의 데이터에 선언적으로 바인딩할 수 있는 HTML기반 템플릿 구문을 사용
> 
> < 종류 >
> 1. Text Interpolation
> 2. Raw HTML
> 3. Attribute Bindings
> 4. JavaScript Expression
>


### 1. Text Interpolation

- 바인딩의 가장 기본적인 형태
- 이중 중괄호구문 (콧수염구문) 을 사용
- 콧수염구문은 해당 구성요소 인스턴스의 msg속성 값으로 대체


### 2. Raw HTML  (많이 사용되진 않음)

- v-html=" "   // const rawHtml = ref('<span style="color:red">   </span>')
- 콧수염구문은 데이터를 일반 텍스트로 해석하기 때문에 실제 HTML을 출력하려면 v-html을 사용해야함


### 3. Attribute Bindings

- v-bind:id="dynamicId"  // const dynamicId = ref('my-id')  => 최종 id는 my-id
- HTML의 id속성 값을 vue의 dynamicld 속성과 동기화 되도록함
- null은 요소에서 id값 제거


### 4. JavaScript Expression

- Vue는 모든 바인딩 내에서 JS 표현식의 모든 기능을 지원
  ```
      <p>message: {{msg}}</p>

      <div v-html="rawHtml"></div>

      <div v-bind:id="dynamicId"> </div>

      <div>{{ number + 1 }}</div>
      <div>{{ ok ? 'Yes' : 'No' }}</div>
      <div>{{ msg.split('').reverse().join('') }}</div> 

      <div v-bind:id="`list-${id}`"></div>

      // 하지만 아래 script에서 처리하고 위는 최종 결과물만 넣는게,,,
  ```

#### 주의사항!
- 각 바인딩에는 하나의 단일 표현식만 포함될 수 있음 
- (return문 뒤에 사용할 수 있는 코드여야함!!)
- const 선언 or if문 XXX

</br>
</br>
</br>

### Directive
- 단일 JS표현식이어야함 (v-for, v-on 제외)
- 표현식 값이 변경될 때 DOM에 반응적으로 업데이트를 적용
- v-if 예시
  - v-if의 값이 True이면 내용 보임 or 내용 안보임


> Directive 전체 구문 (출력에는 나오지X)
>
> v-on:submit.prevent="onSubmit"
> name(directive):argument.Modifiers="Value"
>
> 앞directive(v-on, v-if...)에따라서 argument, 인자는 달라질 수 있음!

- Argument
  - 일부directive 는 directive뒤에 콜론(:)으로 표시되는 인자를 사용할 수 있음
  - ex)
    - v-bind:href    -> href속성값 바인딩
    - v-on:click      -> click이벤트 수신

- Modifiers
  - .(dot)로 표시되는 특수 접미사, 특별한 방시긍로 바인딩 되어야함을 나타냄
  - chaining이 됨! .~.~ 으로 계속 쓸 수 있음
  - ex)
    - .prevent 는 발생한 이벤트에서 event.preventDefault를 호출하도록 v-on에 지시하는 modifiers

- Built-in Directive (공식문서 참고 - 문서 < API 쪽에서 더 자세히 볼 수 있음)
  - https://vuejs.org/api/built-in-directives.html


</br>
</br>

> ## Dynamically data binding

### 1. v-bind
  - 하나 이상의 속성 또는 컴포넌트 데이터를 표현식에 동적으로 바인딩


  1. Attribute Binding
    - HTML의 속성값을 Vue의 상태 속성 값과 동기화 되도록함
    - : 으로 축약해서 씀
    - Dynamic attribute name (동적 인자 이름)
      - 대괄호로 감싸서 directive argument에 JS표현식을 사용할 수도 있음
      - []안의 이름은 반드시 소문자!! (브라우저가 소문자로 강제 변환, 렌더링안됨)

  2. class and Style Binding
    - 클래스 스타일은 모두 속성이므로 v-bind를 사용하여 동적으로 문자열 값 할당 가능
    - but, 단순히 문자열연결은 번거롭 + 오류발생 쉬움
    - -> 객체 또는 배열을 활용할 개선사항 제공

    1. Binding HTML Classes
       1. Objects
          객체를 :class에 전달하여 클래스를 동적으로 전환할 수 있음
          - <div :class="{active: isActive}">Text</div>
          - isActive가 True이면 class에 active추가, false면 추가X
          - 
          - <div class="static" :class="{active: isActive, 'text-primary': hasInfo}">Text</div>
          - 기존에 있던 class에 추가하려면 뒤에 붙여서 쓰면 됨 + 여러개 추가가능
          -  
          - const classObj = ref({active: isActive, 'text-primary': hasInfo })
          - 선언 안에 넣어주고 :class="classObj" 추가해도 됨 (ㅊㅊ)

       2. Arrays
          class를 배열에 바인딩하여 클래스 목록을 적용할 수 있음
          ```
            <div :class="[activeClass, infoClass]">Text</div>
            <div :class="[{active: isActive}, infoClass]">Text</div>


            const isActive = ref(false)
            const hasInfo = ref(true)
            const classObj = ref({
              active: isActive, 
              'text-primary': hasInfo
              })
            const activeClass = ref('active')
            const infoClass = ref('text-primary')
          ```

    2. Binding Inline Styles
       1. Objects
          - style은 JS객체 값에 대한 바인딩을 지원
            ```
              <div :style="{ color: activeColor, fontSize: fontSize + 'px'}">Text</div>
              <div :style="{ 'font-size': fontSize + 'px'}">Text</div>
              <div :style="styleObj">Text</div>

              setup() {
                const activeColor = ref('crimson')
                const fontSize = ref(50)
                const styleObj = ref({
                  color: activeColor,
                  fontSize: fontSize.value + 'px
              })
              // fontSize .value주의!!!!
            ```
        2. Arrays
       
            ```
              <div :style="[styleObj, styleObj2]">Text</div>
              const styleObj2 = ref({ color: 'blue', border: '1px solid black' })

            ```


### v-on
1. Inline handlers : 이벤트가 트리거 될 때 실행 될 JS 코드
2. Method handlers : 컴포넌트에 정의된 메서드 이름
3. v-on약어 : @

```
<div id="app">
    <!-- Inline Handlers : 간단한 상황에 사용 -->
    <button v-on:click="count++">Add 1</button>
    <p>Count: {{ count }}</p>

    <!-- Method Handlers -->
    <button @clcik="myFunc">Hello</button>

    <!-- Calling Methods in Inline Handlers -->
    <!-- 인자를 직접 넣어서 사용할 수 있음 -->
    <button @click="greeting('hello')">Say hello</button>
    <button @click="greeting('bye')">Say bye</button>

    <!-- Accessing Event Argument in Inline Handlers -->
    <!-- 내부변수 : $, event객체 두번째로 들어감, 많이쓰지는 않음 -->
    <button @click="waring('경고입니다.', $event)">Submit</button>

    <!-- event modifiers -->
    <form @submit.prevent="onSubmit">
      <input type="submit">
    </form>
    <a @click.stop.prevent="onLink">Link</a>

    <!-- key modifiers -->
    <!-- 키보드 이벤트는 문법 주의! - MDN keyboardEvent 확인하기! -->
    <input @keyup.enter="onSubmit" type="text">
  </div>

    setup() {
      const count = ref(0)
      const name = ref('Alice')
      const myFunc = function (event) {
        console.log(event)
        // button 
        console.log(event.currentTarget)
        console.log(`hello, ${name.value}`)
      }
      const greeting = function (message) {
        console.log(message)
      }
      const waring = function (message, event) {
        console.log(message)
        console.log(event)
      }
      const onSubmit = function (event) {
        console.log(event)
      }
    }

```


### Form Input Bindings
form을 처리할 때 사용자가 input에 입력하는 값을 **실시간**으로 JS상태에 동기화해야하는 경우(양방향 바인딩)
< 방법 >
1. v-bind와 v-on을 함께 사용
2. v-model 사용


1. v-bind와 v-on을 함께 사용
   - v-bind를 사용하여 input요소의 value 속성 값을 입력 값으로 사용
   - v-on을 사용하여 input 이벤트가 발생할 때마다 input요소의 value값을 별도 반응형 변수에 저장하는 핸들러를 호출
    ```
      <input type="text" @input="onInput" :value="inputText1">
      <p>{{ inputText1 }}</p>

      const inputText1 = ref('')
      const onInput = function (event) {
        inputText1.value = event.currentTarget.value
      }
    ```

2. v-model : 위에것 한방에 사용가능
   - form input요소 또는 컴포넌트에서 양방향 바인딩을 만듦
   - 영어 이외의 단어는 약간 이상하게 나옴! -> 한
    ```
    <input type="text" v-model="inputText2">
    <p>{{ inputText2 }}</p>

    const inputText2 = ref('')
    ```

    ```
    <div id="app">
      <!-- single checkbox -->
      <input type="checkbox" id="checkbox" v-model="checked">
      <label for="checkbox">{{ checked }}</label>

      <!-- multiple checkbox -->
      <div>Checked names: {{ checkedNames }}</div>

      <input type="checkbox" id="alice" value="Alice" v-model="checkedNames">
      <label for="alice">Alice</label>

      <input type="checkbox" id="bella" value="Bella" v-model="checkedNames">
      <label for="bella">Bella</label>

      <!-- single select 옵션자체가 value로 들어감-->
      <div>Selected: {{ selected }}</div>

      <select v-model="selected">
        <option disabled value="">Please select one</option>
        <option>Alice</option>
        <option>Bella</option>
        <option>Cathy</option>
      </select>
    </div>


    const checked = ref(false)
    const checkedNames = ref([])
    const selected = ref('')
    ```


<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>



const { createApp, ref } = Vue

const app = createApp({
  setup() {


    return {

    }
  }
})

app.mount('#app')
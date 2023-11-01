# 11.1 (수) Vue day1

> Front-end Development
> 웹사이트와 웹 어플리케이션의 사용자 인터페이스(UI)와 사용자경험(UX)을 만들고 디자인하는 것
> 
> HTML, CSS, JS 등을 활용하여 사용자가 직접 상호작용하는 부분을 개발


## Client-side fameworks
: 클라이언트 측에서 UI와 상호작용을 개발하기 위해 사용되는 JS기반 프레임워크
( Anguler?, Vue, React)



왜 필요?? -> 웹에서 하는 일이 많아짐 
- 무언가를 읽는 곳 -> 하는 곳
  - ex) 음악스트리밍, 영통 등 복합적이고 대화형 으로 변함 : 
  - 사이트 -> 웹 어플리케이션 이라 부름 , 그래서 매우 동적이 대화형 어플리케이션을 훨씬 더 쉽게 구축할 수 있게 됨
- 다루는 데이터가 많아졌다
  - ex) 친구가 이름변경? -> 친구목록, 타임라인, 스토리 등 모든곳을 바꿔야함
  - 앱의 기본 데이터를 안정적으로 추적하고 업데이트 하는 도구가 필요!
  - 즉, 상태를 변경할 때마다 일치하도록 UI를 업데이트 해야함!


## SPA (Single Page Application)
: 하나의 페이지로 구성된 웹 어플리케이션!
웹 어플리케이션의 초기 로딩 후 새로운 페이지 요청 없이 동적으로 화면을 갱신하며 사용자와 상호작용하는 웹 어플리케이션 (CSR 방식 - 클라이언트에서 화면을 렌더링하는 방식 <-> SSR - 이때까지 우리가 했던 것(장고에서 우리가 만들어서 보내줌, redirect))


#### CSR 방식
1. 브라우저는 페이지에 필요한 최소한의 HTML페이지와 JS를 다운
2. JS를 사용하여 DOM을 업데이트하고 페이지를 렌더링
3. => 변경이 필요하면 AJAX request를 보냄(axios 라이브러리 이용) -> Json 형태로 응답 -> 페이지가 일부만 업데이트

4. 장점
   1. 빠른 속도 (서버로 전송되는 데이터 양도 적어짐, 일부만 렌더링)
   2. 사용자 경험
   3. 프엔, 백엔 명확한 분리 -> 대규모 앱 개발, 유지관리 가능

5. 단점
   1. 초기 구동속도가 느림
   2. SEO(검색엔진 최적화) 문제 - 나중에 그려나가는 것이므로 검색에 잘 노출X
  


어떻게 하나만으로 가능?
-> 최초에 sever에 html만 요청하고 그 이후에 요청X
대신 Ajex요청 후, json파일만 받아옴 (비동기적인 JS 요청으로 하나의 페이지를 유지하지만 데이터를 새로 그리고 지우고 해주어서 사용자가 하나의 페이지인지 모름)
- 즉, 브라우저가 페이지를 로드하면 Vue 프레임워크는 각 HTML 요소에 적절한 JS코드를 실행

</br>
</br>
</br>

> ## [Vue](https://vuejs.org/)
> 사용자 인터페이스를 구축하기 위한 JS 프레임워크!
> 
> 2014 시작, 최신 - Vue3 이니까 Vue2꺼 보지 않기 주의
>
> 사용방법 => CDN or NPM 설치



- 쉬운 학습곡선 및 간편한 문법
- 반응형시스템
- 모듈화 및 유연한 구조



> ### 구조 분해 할당
> 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법


### Vue 의 2가지 핵심 기능
1. 선언적 렌더링 (Declarative Rendering)
   - Html을 확장하는 템플릿구문 {{ }} 을 사용하여 Html이 JS데이터를 기반으로 어떻게 보이는지 설명할 수 있음
  
2. 반응형 (Reactivity)
   - JS상태 변경사항을 자동으로 추적하고 변경사항이 발생할 때 DOM을 효율적으로 업데이트


### Vue 작성방법:
1. CDN 및 APP instance 작성하기
   - const { createApp } = Vue
  
2. createApp 함수로 instance 생성하는 것부터 시작!
   - const app = createApp({ })
   - createApp 내부 = 컴포넌트!
   - 컴포넌트 내 setup() {} 함수 선언 필요, 객체를 반환해야함
   - 반환된 속성만 사용할 수 있음 , {{}} 로 동적 텍스트 렌더링!, JS문법 사용가능
   
3. 컨테이너 요소에 앱 인스턴스를 탑재(연결), 각 인스턴스에 대해 mount는 한번만 호출가능
   - app.mount('#idname')


#### ref() = reactive reference
- 반응형 상태(데이터)를 선언하는 변수
- 인자를 받아 .value 속성이 있는 ref 객체로 래핑하여 반환
- ref로 선언된 변수의 값이 변경되면, 해당 값을 사용하는 템플릿에서 자동으로 업데이트
- 인자는 어떠한 타입도 가능
- 템플릿의 참조에 접금하려면 setup함수에서 선언 및 반환 필요
- 템플릿에서 ref 를 사용할때는 .value를 작성할 필요 없음 (자동으로 풀어줌)


```
  const { createApp, ref } = Vue

  const app = createApp({
    setup () {
      return {
        
      } // 객체 return
    }
  })

  app.mount('')

  // 이때
    const app = createApp({
    setup () {
      // 반응형
      const message1 = ref('hello vue!')

      // 변경 안됨
      const message2 = 'hello vue!' 

      console.log(message) // ref 객체
      console.log(message.value) // hello vue!
      // html 접근은 그냥 {{ message }} 사용

      return {
        message1,
        message2,
      } // 객체 return
    }
  })

```

### eventListener In Vue

```
<body>
  <div id="app">
    <button v-on:click="increment">{{ count }}</button>
    <button @:click="increment">{{ count }}</button>
  </div>

  <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>

  <script>

    const { createApp, ref } = Vue

    const app = createApp({
      setup () {
        const count = ref(0)
        const increment = function () {
          count.value++
          // value 값으로 접근해야함!! 주의!!
        }
        return {
          count,
          increment,
        } // 객체 return
      }
    })

    app.mount('#app')

  </script>
</body>
```

### Ref unwrap 주의사항!!
- 템플릿에서의 unwrap은 ref가 최상위 속성인 경우에만 적용가능!
  ```
  const object = { id: ref(0) }
  
  {{ object.id + 1 }}

  // [object Object] 1
  ```
  - object는 최상위 속성이지만 object.id는 그렇지 않음
  - 표현식을 평가할 때 object.id가 unwrap되지 않고 ref 객체로 남아있기 때문
  ```
    const { id } = object
    
    {{ id + 1 }}
    // 이렇게 분해해주어야함!
    // 그냥 최종값이면 상관없음
  ```


#### Why Refs????
-> 굳이? 이지만 실시간 업데이트가 필요( 변경사항 감지 + 추적 + 실시간업데이트 )


```

  <div id="app">
    <p>반응성 변수: {{ reactiveValue }} </p>
    // nomalvalue값은 console에서는 바뀌지만 화면에서는 바뀌지 않음
    <p>일반 변수: {{ nomalvalue }} </p>
    <button @click="increment">값 업데이트</button>
  </div>


  const { createApp, ref } = Vue

  const app = createApp({
    setup () {
      const reactiveValue = ref(0)
      let nomalvalue = 0

      const increment = function () {
        reactiveValue.value++
        nomalvalue.value++
        console.log(nomalvalue)
      }
      return {
        reactiveValue,
        nomalvalue,
        increment
      }
    }
  })

  app.mount('#app')

```







Vue -> 속성, 메서드있음
정적메서드 - 객체를 따로 만들지 않아도 호출할 수 있음

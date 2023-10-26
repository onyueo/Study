# 10.26 (목)

> ## EVENT
> 무언가 일어났다는 신호!
> 모든 DOM 요소가 이러한 이벤트를 만들어냄
>

웹에서의 이벤트 : 
- 버튼을 클릭했을 때 팝업 창이 출력되는 것
- 드래그앤 드롭
- 키보드입력 -> 새로운 요소 생성

### 1. event object
   - DOM에서 이벤트가 발생했을 때 생성되는 객체
   - 모든 DOM요소는 event를 받고 받은 이벤트를 '처리(event handler)'할 수있음



### 2. Event handler
- 이벤트가 발생했을 때 실행되는 함수
- 사용자의 행동에 따라 어떻게 반응할지를 JS 코드로 표현

> .addEventListener()
- 앞에 DOM요소를 붙임
- 대표적인 이벤트 핸들러 중 하나
- 특정 이벤트를 DOM요소가 수신할 때마다 콜백함수를 호출
- 콜백함수 : 어떠한 외부함수의 인자로 들어가는 함수
  

### 3. EventTarget.addEventListener(type, handler)
- EventTarget : DOM요소
- type : 수신할 이벤트 (명시된 이벤트이름 넣을 것!)
  - 수신할 이벤트 이름, 문자열로 작성 ' '
- handler : 콜백함수  (호출되서 반응할 행동)
  - 발생한 이벤트 객체를 수신하는 콜백함수
  - 어떠한 객체를 유일한 매개변수로 받음
- 대상에 특정 이벤트가 발생하면 지정한 이벤트를 받아 할일을 등록한다
- addEventListener는 this를 본인이 부착한 대상을 가리키도록 설정이 되어있음
  - console.log(this) = 이벤트를 가리킴
  - =>를 쓰면 this가 window를 가리키게됨 주의!

```
  // 1. 버튼 선택 (단일-document, 다중)
  const btn = document.querySelector('#btn')

  // 콜백함수 작성
  const clickCallbackFunc = function (event) {
    console.log(enent)
    console.log(event.currentTarget)
    console.log(this)
    // 모두 <button id="btn">버튼</button>
  }

  // 2. 버튼에 이벤트 핸들러를 부착
  btn.addEventListener('click', clickCallbackFunc)
```

#### Bubbling
: 한 요소에 이벤트가 발생하면 부모요소도 함께 동작함 (가장 최상요소(document)를 만날때까지!)
- 클릭 이벤트가 어디서 발생했든 상관없이 outeroueter까지 이벤트가 버블링되어 핸들러를 실행시키기 때문
- 개발을 편하게 할 수 있는 좋은 현상임

```
<form id="form">
    form
    <div id="div">
      div
      <p id="p">p</p>
    </div>
  </form>

  <script>
    const formElement = document.querySelector('#form')
    const divElement = document.querySelector('#div')
    const pElement = document.querySelector('#p')

    const clickHandler1 = function (event) {
      console.log('form이 클릭되었습니다.')
    }
    const clickHandler2 = function (event) {
      console.log('div가 클릭되었습니다.')
    }
    const clickHandler3 = function (event) {
      console.log('p가 클릭되었습니다.')
    }

    formElement.addEventListener('click', clickHandler1)
    divElement.addEventListener('click', clickHandler2)
    pElement.addEventListener('click', clickHandler3) // p->div->form 순서로 모두 나옴(부모에게도 전파됨)
  </script>
```

- 문제점 : 이벤트가 정확히 어디서 발생했는지 모르게 됨

### 4. target, currentTarget 

```
  <div id="outerouter">
    outerouter
    <div id="outer">
      outer
      <div id="inner">inner</div>
    </div>
  </div>

  <script>
    const outerOuterElement = document.querySelector('#outerouter')

    const clickHandler = function (event) {
      console.log('currentTarget:', event.currentTarget.id)
      console.log('target:', event.target.id)
    }

    outerOuterElement.addEventListener('click', clickHandler)
  </script>
```

- inner를 선택했을 때:
  - target : inner
  - currentTarget : outerouter
- outer를 선택했을 때:
  - target : outer
  - currentTarget : outerouter
- outerouter를 선택했을 때:
  - target : outerouter
  - currentTarget : outerouter

#### 즉, currentTarget 이벤트리스너가 부착된 객체!!
#### target 은 실제 이벤트가 발생한 위치!

- target :
  - 이벤트가 발생한 가장 안쪽의 요소(target)를 참조하는 속성
  - 실제 이벤트가 시작된 target요소
  - 버블링이 진행되어도 변하지 않음
  
- currentTarget :
  - '현재'요소
  - 항상 이벤트 핸들러가 연결된 요소만을 참조하는 속성
  - this와 같음
  - 주의사항 : 
    - console.log로 출력한 경우 null 값을 가짐
    - currentTarget은 이벤트가 처리되는 동안에만 사용할 수 있기때문 (지나가버림)
    - currentTarget이후의 속성값은 target 참고해서 사용하기

- .preventDefault()
  - 이벤트가 동작하지 못하게 막아놓음



### click 이벤트 실습!

#### click - < 버튼을 클릭하면 숫자를 1씩 증가 >

```
<button id="btn">버튼</button>
  <p>클릭횟수 : <span id="counter">0</span></p>



  // 1. 초기값 할당
  let counterNumber = 0

  // 2. 버튼 요소 선택
  const btn = document.querySelector('#btn')

  // 3. 콜백 함수 (버튼에 클릭 이벤트가 발생할때마다 실행할 코드)
  const clickHandler = function () {
    // 3.1 초기값 += 1
    counterNumber += 1

    // 3.2 span 요소를 선택
    const spanTag = document.querySelector('#counter')

    // 3.3 span 요소의 컨텐츠를 1 증가한 초기값으로 설정
    spanTag.textContent = counterNumber
  }

  // 4. 버튼에 이벤트 핸들러 부착 (클릭 이벤트)
  btn.addEventListener('click', clickHandler)

```


#### input - < 사용자의 입력 값을 실시간으로 출력하기 >

```
  <input type="text" id="text-input">
  <p></p>

  <script>
    // 1. input 요소 선택
    const inputTag = document.querySelector('#text-input')

    // 2. p 요소 선택
    const pTag = document.querySelector('p')

    // 3. 콜백 함수 (input 요소에 input 이벤트가 발생할때마다 실행할 코드)
    // 3.1 작성하는 데이터가 어디에 누적되고 있는지 찾기
    const inputHandler = function (event) {
      console.log(event)
      console.log(event.currentTarget)  // input tag
      // 사용자가 입력한 전체 text를 알아내기위해서 input tag의 속성 값들을 확인하기 = value
      console.log(event.currentTarget.value) // console.log(event.this.value)
      
      // 3.2 p요소의 컨텐츠에 작성하는 데이터를 추가
      pTag.textContent = event.currentTarget.value
    
    }

    // 4. input 요소에 이벤트 핸들러 부착 (input 이벤트)
    inputTag.addEventListener('input', inputHandler)

  </script>
```


#### click & input < 사용자의 입력값을 실시간으로 출력 + 클릭하면 스타일 변경 >
```
  <h1></h1>
  <button id="btn">클릭</button>
  <input type="text" id="text-input">



    // input 구현
    const inputTag = document.querySelector('#text-input')
    const h1Tag = document.querySelector('h1')

    const inputHandler = function (event) {
      h1Tag.textContent = event.currentTarget.value
    }

    inputTag.addEventListener('input', inputHandler)


    // click 구현
    const btn = document.querySelector('#btn')
    
    const clickHandler = function (event) {
      // h1Tag.classList.add('blue')

      // toggle
      h1Tag.classList.toggle('blue')
      
    }

    btn.addEventListener('click', clickHandler)

```


#### < Todo 실습 >
```
  <input type="text" class="input-text">
  <button id="btn">+</button>
  <ul></ul>


  <script>
    // 1. 필요한 요소 선택
    const inputTag = document.querySelector('.input-text')
    const btn = document.querySelector('#btn')
    const ulTag = document.querySelector('ul')

    const addTodo = function (event) {
      // 2.1 사용자 입력 데이터 저장
      const inputData = inputTag.value

      // 사용자 입력 데이터가 빈 데이터인지 확인
      if (inputData.trim()) {
        // 2.2 데이터를 저장할 li 요소를 생성
        const liTag = document.createElement('li')
    
        // 2.3 li 요소 컨텐츠에 데이터 입력
        liTag.textContent = inputData
        // console.log(liTag)
  
        // 2.4 li 요소를 부모 ul 요소의 자식 요소로 추가
        ulTag.appendChild(liTag)
  
        // 2.5 todo 추가 후 input의 입력 데이터는 초기화 (선택사항)
        inputTag.value = ' '
      } else  {
        window.alert('투두를 입력하세요!')
      }

    }

    // 2. 버튼에 이벤트 핸들러를 부착
    btn.addEventListener('click', addTodo)
```

#### < 로또 번호 생성기 >
- JS에는 random, range, sample 도 없음! -> 추가 라이브러리 필요
- 우리 : 설치X, CDN으로 가져옴, 공식문서 읽어보기 - array
```
<h1>로또 추천 번호</h1>
  <button id="btn">행운 번호 받기</button>
  <div></div>

  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  <script>
    // 1. 필요한 요소 선택
    const btn = document.querySelector('#btn')
    const divTag = document.querySelector('div')

    // 2. 로또 번호를 생성(+ 태그 만들고 출력까지)하는 함수
    const getLottery = function (event) {
      // 2.1 1부터 45까지의 값이 필요
      const numbers = _.range(1, 46)

      // 2.2 45개의 요소가 있는 배열에서 6개 번호 추출
      const sixNumvers = _.sampleSize(numbers, 6)

      // 2.5 6개의 li 요소를 담을 ul 요소 생성
      const ulTag = document.createElement('ul')

      // 2.3 추출한 번호 배열을 "반복"하면서 li 요소를 생성
      sixNumvers.forEach(function (number) {
        // 2.4 번호를 담을 li 요소 생성 후 입력
        const liTag = document.createElement('li')
        liTag.textContent = number

        // 2.6 만들어진 li를 ul 요소에 추가
        ulTag.appendChild(liTag)
      });

      // 2.7 완성한 ul 요소를 div 요소에 추가
      divTag.appendChild(ulTag)
    }

    // 3. 버튼 요소에 이벤트 핸들러를 부착
    btn.addEventListener('click', getLottery)
  </script>
```




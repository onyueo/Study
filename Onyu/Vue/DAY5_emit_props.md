# 11.08(수)

> ## 1. Passing Props
> ## 2. Component Events
>

<br>
<br>

## 1. Passing Props

같은 데이터 but, 다른 컴포넌트!

동일한 데이터를 사용하지만 화면에 나오는 모양은 다름, 사진을 변경해야할 때 모든 컴포넌트에대해 변경을 해야함 -> 유지보수 힘듦

-> 공통된 부모 컴포넌트에서 관리하자!! == Passing Props


부모는 자식에게 데이터를 전달(Pass Props)하며, 자식은 자신에게 일어난 일을 부모에게 알림(Emit event) 

(데이터를 직접적으로 전달하지 않고, 이벤트가 발생하면 알림 + 부모가 이벤트 감지 )

#### < Props >
=> 부모 컴포넌트로부터 자식 컴포넌트로 데이터를 전달하는데 사용되는 속성

#### < One-Way Data Flow >
=> 모든 props는 자식 속성과 부모 속성 사이에 하향식 단방향 바인딩을 형성

-> 단방향인 이유?

하위 컴포넌트가 실수로 상위 컴포넌트의 상태를 변경하여 앱에서의 데이터 흐름을 이해하기 어렵게 만드는 것을 방지하기 위함!


<br>
<br>

> ### Props 특징
- 속성 업데이트 시 부모 -> 자식 가능 // 반대는 안됨 
- 즉, 자식 컴포넌트 내부에서 props를 변경하려고 시도도 하지 말기 + 불가능
- 부모 컴포넌트가 업뎃될때마다 자식 컴포넌트의 모든 prots가 최신값으로 업데이트 됨!

<br>
<br>
<br>
<br>

pjt 시작 복습!
- npm create vue@latest
- cd vue-project
- npm install
- 초기 생성된 컴포넌트 모두 삭제
- src/assets 내부파일 모두 삭제
- main.js import css 삭제
- App.vue 기본세팅 지우고 vbase-3-~ 셋팅
- npm run dev


> Props 실습
>

- 부모 컴포넌트에서 보낸 props를 사용하기 위해서는 자식 컴포넌트에서 명시적인 props선언이 필요
- 부모에게 import + 이름 적어주기 : props이름="props값"
- 
  1. 문자열 배열을 사용한 선언
   - script에 defineProps(['props이름']) 
   - '-' -> '대문자값'으로 바꾸기 html 속성값에서 -> JS 속성값 으로 바뀌기때문에 이름 변경 주의!!
    - 
  2. 객체를 사용한 선언 (권장!!)
   - script에 defineProps({'props이름': String, ... }) 


Props data를 script에서 사용하려면 props를 const 선언해주어 return값을 받으면 됨!!
  

#### Props 세부사항
1. Props name casing (이름 컨벤션)
   - 선언 및 템플릿 참조 시 (-> camelCase , JS)
   - 자식 컴포넌트로 전달 시 (-> kebab-case, HTML)
2. Static Props & Dynamic Props
   - ??? 정리


<br>
<br>
<br>
<br>
<br>

## 2. Component Events

부모 -> 자식 : 데이터 전달

자식 -> 부모 : 자신에게 일어난 일 알림(소리침) -> 이벤트 요청

소리치는 방법? : emit 메서드

### $emit()
자식 컴포넌트가 이벤트를 발생시켜 부모 컴포넌트로 데이터를 전달하는 역할의 메서드

(소리침 + 데이터 전달 가능!)

'$' : Vue 인스턴스나 컴포넌트 내에서 제공되는 전역 속성이나 메서드를 식별하기 위한 접두어


### emit 구조

$emit(event, ...args)
- event
  - 커스텀 이벤트 이름
- args
  - 추가 인자


> ### 이벤트 발신 및 수신
>

- 발신 (자식-JS)
  - <button @click="$emit('someEvent')"> 클릭 </button>
  
- 수신 (부모-HTML)
  - <ParentComp @some-event="someCallback" />


버블링이 일어나지 않기 때문에 자식-자식은 중간단계에서 선언 필요!


> ### 'emit' Event 선언
> 지금까지 호출-듣기 로 끝남 // emit도 유효성검사 가능 -> 선언!
>

- defineEmits() 사용하여 명시적으로 발신할 이벤트 선언가능
- script에서 $emit메서드를 접근할 수 없음 -> defineEmits()는 $meit 대신 사용할 수 있는 동등한 함수를 반환!
- const emit = defineEmits(['someEvent', 'myFocus'])
- const buttonClick = function() { emit('someEvent') }


### Event Name Casing
- 선언 및 발신 시 (camelCase)
  - <button @click="buttonClick"> 클릭 </button>
  - 
  - const emit = defineEmits(['someEvent'])
  - const buttonClick = function() { emit('someEvent') }

- 부모 컴포넌트 수신 시 (kebab-case)
  - ParentChild 에 @emit-args="getNumvers" 추가
  - const getNumvers = function(...args) { .... }



> 실습 구현 : 최하위 자식에서 부모에 있는 값 변경 요청
>

### 주의사항!
- num-props="1"  -> 문자열 "1" 전달
- num-props=1  -> 숫자 1 전달

- props는 객체선언 문법 권장!
  - 가독성 좋아짐
  - 잘못된 유형전달 시 경고 가능
  - 유효성검사 활용가능
- 
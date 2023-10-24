# 10.24 (화)

# Basic syntax of JavaScript

## > 변수명 작성 규칙
- 반드시 문자, 달러($), 밑줄(_) 로 시작
- 대소문자 구분
- 예약어 사용 불가 (for, if, function)
</br>

- 카멜 케이스(camelCase) -> 가장 많이 사용!
  - 변수, 객체, 함수 에 사용
- 파스칼 케이스(PascalCase)
  - 클래스, 생성자에 사용
- 대문자 스테이크 케이스(SNAKE_CASE)
  - 상수(constants)에 사용
  
## > 변수 선언 키워드
1. **let**
   - 블록스코프를 갖는 지역변수를 선언 // 블록 = 중괄호{}
   - 중괄호 안에선언한 변수와 밖에 선언한 변수를 서로 영향을 끼치지 않는다
   - 재할당 가능 (가변 )
   - 재선언 불가능 (let 똑같은 값 두번 쓸수X)

2. **const**
   - 블록스코프를 갖는 지역변수를 선언
   - 재할당 불가능
   - 재선언 불가능
   - 초기값 없이 선언불가능
  
3. **var**
  - 안쓸것,,

```
// let
    let number = 20
    console.log(number)   // 20
    number = 30         // 재할당 가능
    let number = 10     // 재선언 불가능


    // const
    const num = 10
    num = 20
    console.log(num)    // type error - 재할당 불가능
    const num = 30    // 재선언 불가능

```

   
> #### 기본적으로 const 사용 권장
> #### 재할당이 필요한 변수정도만 let으로 변경해서 사용
> </br>
> 
</br>

## block scope
- if, for, 함수 등의 중괄호{} 내부 를 가리킴
- 블록스코프를 가지는 변수는 블록 바깥에서 접근 불가능
- 파이썬이 영역을 들여쓰기로 구분했다면 JS는 중괄호로 영역 분리
- 중괄호 내부, 외부는 서로 다른 영역에 있기 때문에 접근불가 + 영향끼치지X
  
</br>
</br>
</hr>

> ## > 데이터 타입
> 1. **원시 자료형**
>   - Number, String, Boolean, undefined, null
>   - 변수에 값이 직접 저장되는 자료형 ( 불변, 값이 복사)
> 
> 2. **참조 자료형** 
>   - Objects(Object=dictionary, Array, Function)
>   - 객체의 주소가 저장되는 자료형 (가변, 주소가 복사)
> </br>

</br>
</br>

### 1. 원시자료형 (number)
- Number, String, Boolean, undefined, null
- 변수에 값이 직접 저장되는 자료형 ( 불변, 값이 복사)
  
```
<!-- 원시 자료형 -->

// EX1
const bar = 'bar'
console.log(bar)    // bar

bar.toUpperCase()   // 대문자변환
console.log(bar)    // bar = 불변

// EX2
let a = 10
let b = a
b = 20

console.log(a)    //10
console.log(b)    //20



<!-- 참조 자료형 -->

const obj1 = {name: 'Alice', age:30}
const obj2 = obj1
obj2.age = 40

console.log(obj1.age)   //40    주소복사, 가변
console.log(obj2.age)   //40

```

- Number (정수 또는 실수를 표현하는 자료형)
  - Infinity : 양의 무한대
  - -Infinity : 음의 무한대
  - NaN : Not a number

- String (텍스트 자료형)
  - '+' 연산자를 사용해 문자열끼리 결합
  - 곱셈, 나눗셈, 뺄셈 불가능

> Template literals (템플릿 리터럴) == f-string
  - 내장된 표현식을 허용하는 문자열 작성 방식
  - 백틱(``)을 이용하며, 여러줄에 걸쳐 문자열을 정의할 수도있고, JS의 변수를 문자열 안에 바로 연결할 수 있음
  - 표현식은 '$ '와 중활호 (${~~}) 로 표기
  - ex) const message = '`안녕하세요 ${name} 입니다`'
  - ES6+ 부터 지원!! (<- 이부부터 편리해짐!)


> null과 undefined
> 값이 없음을 표현하는 데이터타입



- **null** : 변수의 값이 없음을 의도적으로 표현할 때 사용 (개발자가 의도적으로 넣음)
- **undefined** : 변수선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨 (JS 가 넣음)
- 두개를 구분해놓은 이유? - 초기 설계 실수

```
// null
let a = null
console.log(a)  // null

//undefined
let b
console.log(b)   //undefined
```

- **Boolean**
  - 조건물 또는 반복문에서 boolean이 아닌 데이터타입은 "자동 형변환 규칙"에 따라 True 또는 False로 변환됨
  
|데이터타입|false|true|
|----|-----|-----|
|undefined|항상 false|X|
|null|항상 false|X|
|Number|0, -0, NaN|나머지 모든 경우|
|String|빈문자열|나머지 모든 경우|


### Javascript data type MDN 검색ㄱ (문법과 자료형)


### 할당 연산자
- '+, -, *, %' 사용가능
  
```
let a = 0
a += 10  // a = 10

a -= 3  // a = 7

*, % 지원
```

- **증가연산자** (++)
  - 피연산자를 증가(1을 더함) 시키고, 연산자의 위치에 따라 증가하기 전이나 후의 값을 반환
- **감소연산자** (--)
  - 피연산자를 감소(1을 뺌)시키고 연산자의 위치에 따라 감소하기 전이나 후의 값을 반환

- += 또는 -= 와 같이 더 **명시적인 표현으로 작성하는것을 권장**

```
let x = 3
const y = x++
console.log(x, y)   // 4, 3

let a = 3
const b = ++a
console.log(a, b)   // 4, 4
```

- **동등 연산자(==)**
  - 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
  - 암묵적 타입 변환을 통해 타입을 일치시킨 후 같은 값인지 비교
  - 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별
  ```
  1 == 1    //true
  'hello' == 'hello'    //true
  '1' == 1    //true
  0 == false    //true
  ```

- **일치 연산자 (===) -> 권장!!**
  - 두 피연산자의 값과 타입이 모두 같은 경우 true를 반환
  - 같은 객체를 가리키거나, 같은 타입이면서 같은 값인지 비교
  - 엄격한 비교가 이루어지며, 암묵적 타입변환이 발생하지 않음
  - 특수한 경우를 제외하고는 동등연산자가 아닌 **일치 연산자 사용권장**
  ```
  1 == 1    //true
  'hello' == 'hello'    //true
  '1' == 1    // false
  0 == false    //false
  ```


- **논리 연산자**
  - and : &&
  - or : ||
  - not : !
  - 단축평가 지원


## 조건문
- ### if
```
# 기본 구조
    if ( ) {

    } else if () {

    } else {

    }
```

- 조건(삼항) 연산자
  - 세개의 피연산자를 받는 유일한 연산자
  - 앞에서부터 조건문, 물음표(?), 조건문이 참일경우 실행할 표현식, 콜론(:), 조건문이 거짓일 경우 실행할 표현식이 배치

  ```
    const person = 100
    if (person > 17) {
      return 'yes'
    } else {
      return 'No'
    }

    // 한줄로 바꾸기
    person > 17 ? 'yes': 'No'
  ```

## 반복문
1. while
2. for
3. for..in  순서X
4. for..of  순서O


- ### while
  - 조건문이 참이면 문장을 계속해서 수행
  ```
  // while
  let i = 0
  while( i < 6 ) {
    console.log(i)
    i += 1
  }
  ```

- ### for
  - 특정한 조건이 거짓으로 판별될 때까지 반복
  ```
  // 기본구조
  for ([초기문]; [조건문]; [증감문]) {
      
    }

  // for
  for (let i = 0; i < 6; i++) {
    console.log(i)
  }

  ```

- ### for...in
  - 객체의 열거 가능한 속성(property/key)에 대한 반복
  ```
      // for..in
    const fruits = {
      a: 'apple',
      b: 'banana'
    }

    for (const property in fruits) {
      console.log(property)   // a, b (속성이나옴 //파이썬-keyvalue)
      console.log(fruits[property]) // apple, banana
    }

  ```

- ### for...of
  - 반복 가능한 객체(배열, 문자열 등) 에 대한 반복
  - 순서 O -> 인덱스
  ```
  // for ..of
  const numbers = [3, 2, 1, 0]

  for (const number of numbers) (
  console.log(number)   // 3, 2, 1, 0
  )
  ```

### 배열 반복과 for...in  (순서 X !! ) -> Object 에서만 씀
- 배열의 인덱스는 정수의 이름을 가진 **열거 가능한 속성**
- for..in은 정수가 아닌 이름과 속성을 포함하여 열거 가능한 모든 속성을 반환
- 내부적으로 for..in은 배열의 반복자 대신 속성 열거를 사용하기 때문에 **특정 순서에 따라 인덱스를 반환하는 것을 보장할 수 없음**
  
</br>

- **인덱스의 순서가 중요한 배열에서는 사용하지 않음**
- 배열의 for 반복, for..of 반복을 사용


참조자료형의 object -> 키 : 값

array -> 인덱스 : 순서가 있는 정수

```
// for.. in
    const numbers2 = ['a', 'b', 'c', 'd']
    for (const number in numbers2) {
      console.log(number)   // 0, 1, 2, 3

    }


// for .. of
    const numbers2 = ['a', 'b', 'c', 'd']
    for (const number of numbers2) {
      console.log(number)   // a, b, c, d
    }

```

> ### for .. of  (객체를 제외한 반복가능한 것들)
> Array = ['a', 'b', 'c'] 
>
> ### for .. in (객체)
> Object = {
  a : 'ss',
  b : 'dd',
  c : 'ee'
}


#### 반복문 사용 시 const 사용 여부
- for 문
  - 최초 정의한 i를 재할당 하면서 사용하기 때문에 const는 에러남
- for..in, for...of
  - cost사용해도 에러x
  - 단, const 이용 시 반복문에서 사용한 변수를 내부에서 수정할 수 없음



#### 반복문 종합
|키워드|연관키워드|스코프
|----|----|----|
|while|break, continue| 블록스코프|
|for| break, continue| 블록 스코프|
|for...in|object순회|블록 스코프|
|for...of|Iterable순회|블록 스코프


### 세미콜론
- JS는 세미콜론을 선택적으로 사용가능
- 세미콜론이 없으면 ASI에 의해 자동으로 삽입됨
- 우리는 안쓸것임 + 안써도 ㄱㅊ

### VAR - 변수선언 키워드
- ES6 이전에 사용했던 키워드
- 재할당, 재선언 가능
- 호이스팅되는 특성으로 예기치못한 문제 발생 가능 (유지보수 힘듦)
- 함수 스코프를 가짐
- 변수 선언 시 var, const, let을 사용하지 않으면 자동으로 var 선언됨 -> 변수선언시 const, let 필수 사용해주기!!!

### NaN을 반환하는 경우

> # 아니 이게 된다고?
> # 아니 이게 안된다고?
> # 아니 왜 이렇게 출력하지?




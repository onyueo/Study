# 10.25 함수, 객체

> ## 함수

### 1. 함수 구조
- 함수의 이름
- 함수의 매개변수
- 함수의 body(중괄호 안) 를 구성하는 statment
- return 값이 없다면 undefined를 반환


### 2. 정의방법 (2가지)
- 사용할땐 차이가 없음!


2.1 선언식 : 자주쓰는 함수는 선언식이용
```
fucntion funcName () {
  statement
}

function add(num1, num2) {
  return num1 + num2
}

- 선언보다 함수가 아래있어도 사용 가능 (호이스팅)


```
**2.2 표현식** (사용권장) : 익명, 한번씩 사용할 때?
```
// 기본구조 이렇게 시작!
const 함수이름 = ( ) => {}


const funcName = fucntion () {
  statement
}

const sub = function (num1, num2) {
  return num1 - num2
}
```

- 익명함수(함수이름이 없는것)를 사용할 수 있음
- 호이스팅되지 않으므로 함수를 정의하기 전에 먼저 사용할 수 없음



### 3. 매개변수 정의방법
   1. 기본함수 매개변수
   2. 나머지 매개변수
   
  3.1 기본함수 매개변수
    : 값이 없거나 undefined가 전달될 경우 이름이 붙은 매개변수를 기본값으로 초기화
  ```
    const greeting = function (name = 'Anonymous') {
      return `Hi ${name}`
    }
  ```

  3.2 나머지 매개변수
  : 임의의 수를 인자로 배열로 허용하여 가변인자를 나타내는 방법
  - 규칙
    - 함수 정의 시 나머지 매개변수 하나만 작성할 수 있음
    - 나머지 매개변수는 함수 정의에서 매개변수 마지막에 위치해야함
    - 나머지 매개변수 사용 : ...
  ```
    const myFunc = function (num1, num2, ...restArgs) {
      return [num1, num2, restArgs]
    }
  ```

- 매개변수와 인자의 **개수 불일치 허용**
  - 매개변수 개수 > 인자 개수   (undefined 이용)
  ```  
    const threeArgs = function (num1, num2, num3) {
      return [num1, num2, num3]
    }

    console.log(threeArgs()) // [undefined, undefined, undefined]
    console.log(threeArgs(1)) // [1, undefined,  undefined]
    console.log(threeArgs(2, 3))  /[2, 3, undefined]
  ```
  - 매개변수 개수 < 인자 개수
    - 초과입력한 인자는 사용하지 않음!
    - 에러도 안남
  
### 4. '...' : 전개구문 (spread syntax)
  - 배열이나 문자열과 같이 반복가능한 항목을 펼치는 것 (확장, 전개)
  - 전개 대상에 따라 역할이 다름
    - 배열이나 객체의 요소를 개별적인 값으로 분리하거나
    - 다른 배열이나 객체의 요소를 현재 배열이나 객체에 추가하는 등
  
  1. 함수와의 사용
     1. 함수 호출시 인자 확장
        ```
        function myFunc(x, y, z) {
          return x + y + z
        }

        let numbers = [1, 2, 3]
        console.log(myFunc(...numbers)) // 6
        ```

     2. 나머지 매개변수 (압축)
        ```
        function myFunc2(x, y, ...restArgs) {
          return [x, y, restArgs]
        }

        console.log(myFunc2(1, 2, 3, 4, 5)) // [1, 2, [3, 4, 5]]
        console.log(myFunc2(1, 2)) // [1, 2, []]
        ```

  2. 객체와의 사용 (객체파드에서 진행)
  3. 배열과의 활용 (배열파트에서 진행)


### 5. 화살표 함수 표현식 (단계적으로 생각!)
  ```
    const arrow1 = function (name) {
      return `hello, ${name}`
    }
  ```

**5.1 function 키워드 삭제/제거 후 화살표(=>) 작성  (권장)**
    - ```const arrow2 = (name) => { return `hello, ${name}` }```

  5.2 인자가 1개일 경우에만 () 생략 가능 // (but, 생략 X 권장!)
    - ```const arrow3 = name => { return `hello, ${name}` }```

  5.3 함수 본문이 return을 포함한 표현식 1개일 경우에 {} & return 삭제 가능
    - ```const arrow4 = name => `hello, ${name}` ```

</br>
</br>
</br>
</br>

> ## 객체  (Object: data collector)
: Object = 키로 구분된 데이터 집합을 저장하는 자료형

### 1. 객체 구조
   - 중괄호를 이용해 작성
   - 중괄호 안에는 key:value 쌍으로 구성된 속성(property)를 여러개 작성가능
   - key는 문자형만 허용
   - value는 모든 자료형 허용

  ```
    const user = {
    name: 'Alice',
    'key with space': true,
    greeting: function () {
      return 'hello'
      }
    }
  ```

### Key에 접근하는 방법 2가지
1. 점 ('.', chanining operator)
2. 대괄호[] 로 객체 요소 접근
   - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능
  
```
  console.log(user.name) // Alice
  console.log(user['key with space']) // true
```



### 2. 객체와 함수
Method : 객체 속성에 정의된 함수
- object.method() 방식으로 호출
- 매서드는 객체를 '행동'할 수 있게 함
- ``` console.log(user.greeting()) // hello ```

> ### 3. This
> 함수나 매서드를 호출한 객체를 가리키는 키워드 // 함수가 '호출되는 방식' 에 따라 결정되는 현재 객체를 나타냄
> 함수 내에서 객체의속성 및 메서드에 접근하기 위해 사용
> 함수는 호출될때 암묵적으로 this를 전달받음
> python.의 self 와 Java의 this가 선언 시 값이 이미 정해지는 것에 비해 JS의 this는 함수가 호출되기 전까지 값이 할당되지 않고 호출 시에 결정됨 (동적할당)
>  

- this가 미리 정해지지 않고 호출되는 방식에 의해 결정되는 것은
  - 장점 : 함수(메서드)를 하나만 만들어 여러 객체에서 재사용할 수 있다는 것
  - 단점 : 너무 유연해서 실수로 이어질 수 있음

```
const user = {
    name: 'Alice',
    'key with space': true,
    greeting: function () {
      return 'hello my name is ${this.name}'
    }
  }
  console.log(user.greeting()) // hello my name is Alice
```

- 함수를 호출하는 방법에 따라 가리키는 대상이 다름
  1. 단순호출 : 전역 객체
    ```
    const myFunc = function () {
      return this
    }
    console.log(myFunc()) // window -> 브라우저의 최상위 객체(window > document), 생략가능
    ```

  2. 메서드 호출 : 메서드를 호출한 객체
    ```
    const myObj = {
      data: 1,
      myFunc: function () {
        return this
      }
    }
    console.log(myObj.myFunc()) // myObj
    ```
   3. 중첩된 함수에서의 this 문제점과 해결책
     - 문제점: 일반호출일 때 this가 전역 객체를 가리킴
       ```
         const myObj2 = {
           numbers: [1, 2, 3],
           myFunc: function () {
             this.numbers.forEach(function (number) {
               console.log(this) // window
             })
           }
         }
         console.log(myObj2.myFunc())
       ```
     - 해결책: 화살표함수는 자신만의 this를 가지지 않기 때문에 외부함수에서의 this값을 가져옴(자기 상위함수를 가져옴)
       ```
       const myObj3 = {
         numbers: [1, 2, 3],
         myFunc: function () {
           this.numbers.forEach((number) => {
             console.log(this) // myObj3
           })
         }
       }
       console.log(myObj3.myFunc())
       ```


### 4. 단축속성

4.1 단축 속성 : 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우 단축구문을 이용할 수 있음
4.2 단축 메서드 : 매서드 선언 시 fucntion 키워드 생략 가능
```
    // 단축 속성
    const name = 'Alice'
    const age = 30

    const user = {
      name: name,
      age: age,
    }

    const user = {
      name,
      age,
    }

    // 단축 메서드
    const myObj1 = {
      myFunc: function () {
        return 'Hello'
      }
    }

    const myObj2 = {
      myFunc() {
        return 'Hello'
      }
    }

  ```
4.3 계산된 속성
  - 키가 대괄호로 둘러싸여 있는 속성
  - 고정된 값이 아닌 변수값을 사용할 수 있음
  ```
    const product = prompt('물건 이름을 입력해주세요')
    const prefix = 'my'
    const suffix = 'property'

    const bag = {
      [product]: 5,
      [prefix + suffix]: 'value',
    }

    console.log(bag) // {연필: 5, myproperty: 'value'}
  ```

#### 4.4 구조 분해 할당 (destructing assingment) -> 유용 + 자주씀
: 배열 또는 객체를 분해햐여 속성을 변수에 쉽게 할당할 수 있는 문법

- 변수에 할당했을 때
  - 적용 전
  ```
    // 구조 분해 할당
      const userInfo = {
        firstName: 'Alice',
        userId: 'alice123',
        email: 'alice123@gmail.com'
      }

      const firstName = userInfo.name
      const userId = userInfo.userId
      const email = userInfo.email
  ```

  - 적용 후
  ```
    const userInfo = {
        firstName: 'Alice',
        userId: 'alice123',
        email: 'alice123@gmail.com'
      }

      // const { firstName } = userInfo
      // const { firstName, userId } = userInfo
      const { firstName, userId, email } = userInfo

      // Alice alice123 alice123@gmail.com
      console.log(firstName, userId, email)
  ```

- 함수에 할당했을 때
```
  // 구조 분해 할당 활용 - 함수 매개변수
    function printInfo({ name, age, city }) {
      console.log(`이름: ${name}, 나이: ${age}, 도시: ${city}`)
    }

    const person = {
      name: 'Bob',
      age: 35,
      city: 'London',
    }

    // 함수 호출 시 객체를 구조 분해하여 함수의 매개변수로 전달
    printInfo(person) // '이름: Bob, 나이: 35, 도시: London'

```

4.5 Object with 전개구문
- 객체복사 : 객체 내부에서 객체 전개
- 얕은 복사에 활용 가능
```
  // with 전개 구문
  const obj = { b: 2, c: 3, d: 4 }
  const newObj = { a: 1, ...obj, e: 5 }
  console.log(newObj) // {a: 1, b: 2, c: 3, d: 4, e: 5}
```

4.6 유용한 객체 메서드
- Object.keys()
- Object.values()
```
  // 유용한 객체 메서드
    const profile = {
      name: 'Alice',
      age: 30,
    }

    console.log(Object.keys(profile)) // ['name', 'age']
    console.log(Object.values(profile)) // ['Alice', 30]
```
4.7 Optional chaning ('?.)
- 속성이 없는 중첩 객체를 에러 없이 접근할 수 있음
- 만약 참조 대상이 null 또는 undefined라면 에러가 발생하는 것 대신 평가를 멈추고 undefined를 반환
- 그냥 없는 속성을 .으로 물어보면 typeerror가 나오지만 ?.로 물어보면 undefined로 나옴
- 참조가 누락될 가능성이 있는 경우를 참조해야할 때 미리 예방할 수 있음
- 주의 : 
  - 남용금지!!, 
  - 평가대상이 없어도 괜찮은 경우에만 선택적으로 사용, 
  - Optional chaning 앞의 변수는 반드시 선언되어 있어야 함


</br>
</br>
</br>
</br>

> ## JSON
- JavaScript Object Notation
- key-value 형태로 이루어진 자료 표기법
- JS 의 Object와 유사한 구조를 가지고 있지만 JSON은 형식이 있는 문자열
- JS 에서 JSON을 사용하기 위해선 Object 자료형으로 변경해야함

```
  const jsObject = {
      coffee: 'Americano',
      iceCream: 'Cookie and cream',
    }

    // Object -> JSON
    const objToJson = JSON.stringify(jsObject)
    console.log(objToJson)  // {"coffee":"Americano","iceCream":"Cookie and cream"}
    console.log(typeof objToJson)  // string

    // JSON -> Object
    const jsonToObj = JSON.parse(objToJson)
    console.log(jsonToObj)  // { coffee: 'Americano', iceCream: 'Cookie and cream' }
    console.log(typeof jsonToObj)  // object
```


### new 연산자 활용

- JS 에서 객체를 하나 생성한다고 하면?
  - 하나의 객체를 선언하여 생성
  - 동일한 형체의 객체를 또만들 때 또다른 객체를 선언해야하는 불편함이 있음
  - -> 틀을 만들자 (new!)

```
  function Member(name, age, sId) {
      this.name = name
      this.age = age
      this.sId = sId
    }

    const member3 = new Member('Bella', 21, 20226543)

    console.log(member3) // Member { name: 'Bella', age: 21, sId: 20226543 }
    console.log(member3.name) // Bella
```


</br>
</br>
</br>
</br>

> **##배열 (Array)** (중요!!)
> Object : 키로 구분된데이터 집합을 저장하는 자료형 but, 순서가 없음
> => 순서가 있는 collection이 필요
> Array : 순서가 있는 데이터 집합을 저장하는 자료구조 (key를 index로 가져와서 순서를 만듦)
> 

1. 배열 구조
  - 대괄호[] 를 이용해 작성
  - 배열 요소 자료형 : 제약없음
  - length 속성을 사용해 배열에 담긴 요소가 몇 개인지 알 수 있음 (길이를 잴 수 있음)
  - 음수 인덱스값이 없기때문에 마지막 요소에 접근할때 length속성 활용하기

2. 배열과 메서드
   - push / pop : 배열 끝 요소를 추가 / 제거
   - unshift / shift : 배열 앞 요소를 추가 / 제거
  
- pop() : 배열 끝 요소를 제거하고 제거한 요소를 반환
- push() : 배열 끝에 요소를 추가
- shift() : 배열 앞 요소를 제거하고 제거한 요소를 반환
- unshift() : 배열 앞에 요소를 추가


> ### **3. Array helper method (매우매우 중요)**
> **콜백함수** : 다른함수에 인자로 전달되는 함수!!
> 배열을 순회하며 특정 로직을 수행하는 메서드
> 메서드 호출 시 인자로 함수를 받는 것이 특징 ( 콜백함수 )

- forEach : 인자로 주어진 함수(콜백함수)를 배열 요소 각각에 대해 실행 (map과달리 return이 없음)
  - 배열을 순회하며 각각의 요소에게 함수 실행 // python의 map과 비슷!!
- map : 배열 내의 모든 요소 각각에 대해 함수(콜백함수)를 호출하고, 함수 호출결과를 모아 새로운 배열을 반환


- #### forEach 구조 :
  - 배열.forEach(callback(item[, index[, array]]))
  - 콜백함수는 3가지 매개변수로 구성
  - item : 처리할 배열의 요소
  - index : 처리할 배열 요소의 인덱스 (선택인자)
  - array : forEach를 호출한 배열 (선택인자)
  - 반환값 : undefined
  - **반복문의 연장선**, 배열반복을 통해서 로직을 진행하고자할 때 사용

```
// 화살표 함수 이용하기!!
names.forEach((item, index, array) => {
  console.log(`${item} / ${index} / ${array}`)
})

(item, index, array) => {
  console.log(`${item} / ${index} / ${array}`)
} => 함수!!!

const numbers1 = [1,2,3]

numbers1.forEach(function (num) {
  console.log(num**2)
})   // 1, 4, 9


// 함수 이용해서 사용
const callBack = function (num) {
  console.log(num**2)
}

numbers2.forEach(callBack)
// 1, 4, 9


```

- #### map : forEach와 99% 같음 // 결과물을 새로운 **배열**을 할당하고 반환함!

```
  // 1
  const names = ['Alice', 'Bella', 'Cathy',]

  const result1 = names.map(function (name) {
    return name.length
  })

  const result2 = names.map((name) => {
    return name.length
  })

  console.log(result1) // [5, 5, 5]
  console.log(result2) // [5, 5, 5]


  // 2
  const numbers = [1, 2, 3,]

  const doubleNumber = numbers.map((number) => {
    return number * 2
  })

  console.log(doubleNumber) // [2, 4, 6]
```

### 4. 배열 순회 종합
```
  const names = ['Alice', 'Bella', 'Cathy',]

  // for loop
  for (let idx = 0; idx < names.length; idx++) {
    console.log(idx, names[idx])
  }

  // for ...in -> 객체꺼(순서X) ,배열에서 사용X
  // for...of
  for (const name of names) {
    console.log(name)
  }

  // forEach (사용권장)
  names.forEach((name, idx) => {
    console.log(idx, name)
  })
```
- forEach : 간결하고 가독성 높음, break, continue사용 불가능
- 배열순회필요때 forEach사용!!


### 콜백함수 구조를 사용하는 이유:
1. 함수의 재사용성 측면
   - 함수를 호출하는 코드에서 콜백함수의 동작을 자유롭게 변경할 수 있음
   - map함수는 콜백함수를 인자로 받아 배열의 각 요소를 순회하며 콜백함수를 실행
  
2. 비동기적 처리 측면 (= 병렬 처리, 동시에처리)
   - setTimeout 함수는 콜백함수를 인자로 받아 일정시간이 지난 후에 실행됨 + 다른코드의 실행을 방해하지 않음




## MDN문서 참고해보기!! (Array helper methods)


```
<!-- 오후 수업 -->

    const numbers = [1,2,3,4,5]

    // 기본구조, return 필요X
    numbers.forEach(() => {})

    numbers.forEach((number) => {
      console.log(number)
    }) // 1,2,3,4,5


    // X
    numbers.map((number) => {
      return number*2
    })

    // O
    const r = numbers.map((number) => {
      return number*2
    })
    console.log(r)


    // 필터 - 짝수만 뽑고싶을 때
    const c = numbers.filter((number) => {
      if (number%2 === 0) {
        return true
      }
    })
    console.log(c)

    
    //find
    const f = numbers.find((number) => {
      if (number === 2) {
        return true
      }
    })
    console.log(f)


    //some
    const s = numbers.some((number) => {
      if (number === 2) {
        return true
      }
    })
    console.log(s) // true가 하나라도 있으면 True

    //every
    const e = numbers.every((number) => {
      return number < 10
    })
    console.log(e) // true  (모두가 true여야 true)




  const poeple = [
      {name: 'A', age:20},
      {name: 'B', age:25},
      {name: 'C', age:20},
    ]
  
    // 찍어보고 이해하기!
    poeple.forEach((a, b, c) =>  {
      console.log(a, b, c)
    })


    // 나이가 20인 사람만 추출
    const r = poeple.filter((p) => {
      if (p.age === 20) {
        return true
      }
    })
    console.log(r) //  [{name: 'A', age:20},{name: 'B', age:25},{name: 'C', age:20},]


    // 새로운 요소 생성 후 뽑기
    const c = poeple.map((p) => {
      const newP = p
      newP.city = '광주'
      return newP
    })
    console.log(c)
    // 문제점 : 복사가 일어나서 people도 바뀜!
    r[0].name = 'aaa'

    // 해결1 : (얕은복사?)
    const d = poeple.map((p) => {
      const {name, age} = p
      return {
        name,
        age, 
        city: '광주'
      }
    })

    // 해결2: 전개, ... = 얕은복사
    const k = poeple.map((p) => {
      // const newP = {...p, city: '광주'}
      return newP = {...p, city: '광주'}
    })

```
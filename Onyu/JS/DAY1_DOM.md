# 10.23 (월)
## 오늘의 목표 : 웹 브라우저 안에서 JS사용하기!~
웹페이지의 동적인 기능 구현


> ### 실행 환경 종류
> 1. HTML script 태그
> 2. js 확장자 파일
> 3. 브라우저 Console


### 1.HTML script 태그
- body tag 안에서 script태그를 넣으면 그 안은 JS가 적용!
- 명령어 : console.log('~~')
- 개발자도구의 콘솔창에서 값 확인할 수 있음


### 2. js 확장자 파일
- 새로운 JS파일 만들기
- script태그 안에 src='만든파일.JS' 넣어주기

```
  <!-- 1.HTML script 태그 이용 -->
  <script>
    console.log('Hello World!')
  </script>


  <!-- 2. js 확장자 파일 이용 -->
  <script src="test.js"> </script>
```

### 3. 브라우저 Console
- 개발자도구 콘솔창에서 명령어 : console.log('~~') 치기


> ## DOM
> 웹파이지를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공  (문서구조, 스타일, 내용 등을 변경할 수 있도록 함)
> 프로그래밍 언어에게 모든것을 객체!로 제공함 (요소, 속성, 텍스트 = 객체, 부모자식존재)

- ### 동적으로 만들기 = 문서를 "조작"을 하려면 요소를 "선택" 할 수 있어야 함! 
- -> 각각을 객체로 접근/제공할 수 있어야 함 = DOM 
- 시작명령어 = document.

> 선택 메서드 ('_' 사용X )
>  - 요소 한개 선택 : document.querySelector()
>  - 요소 여러개 선택 : document.querySelectorAll()

### 요소 한개 선택 : document.querySelector()
-> 제공한 선택자와 일치하는 element 한 개 선택
제공한 CSS를 만족하는 첫번째 element 객체를 반환(없다면 null 반환)


### 요소 여러개 선택 : document.querySelectorAll()
-> 제공한 선택자와 일치하는 여러 element선택
제공한 CSS를 만족하는 NodeList [] 반환
- 인덱스로 접근가능, length 도 return



```
  <h1 class="heading">DOM 선택</h1>
  <a href="https://www.google.com/">google</a>
  <p class="content">content1</p>
  <p class="content">content2</p>
  <p class="content">content3</p>
  <ul>
    <li>list1</li>
    <li>list2</li>
  </ul>


 <script>
  document.querySelector('.heading')    # <h1 class="heading">DOM 선택</h1> // 모두 선택
  document.querySelector('.content')    # <p class="content">content1</p>  // 첫번째 값 반환
  document.querySelectorAll('.content')   # NodeList(3) [p.content, p.content, p.content]
  document.querySelectorAll('ul>li')    # NodeList(2) [li, li]
  </script>
```



> ## DOM 조작
> ### 1. 속성조작
> 1.1 클래스 속성 조작  
> 1.2 일반 속성 조작
> 
> ### 2. HTML 콘텐츠 조작
> ### 3. 조작 메서드
> ### 4. Style 조작



1. 클래스 속성 조작(element.classList)
- 요소의 클래스 목록을 유사배열 형태로 반환
- 지정한 클래스 값을 추가 : element.classList.add()
- 지정한 클래스 값을 제거 : element.classList.remove()
- 클래스가 존재하면 제거, false반환/ 존재하지 않으면 추가, True 반환 : element.classList.toggle()


2. 일반 속성 조작
- element.getAttribute()
  - 해당 요소에 지정된 값을 반환(조회)
- element.setAttribute(name, value)
  - 지정된 요소의 속성 값을 설정
  - 속성이 이미 있으면 기존 값을 갱신 else 지정된 이름과 값으로 새 속성값 추가
- element.removeAttribute()
  - 요소에서 지정된 이름을 가진 속성 제거


```
  
  <h1 class="heading">DOM 선택</h1>
  <a href="https://www.google.com/">google</a>
  <p class="content">content1</p>
  <p class="content">content2</p>
  <p class="content">content3</p>
  <ul>
    <li>list1</li>
    <li>list2</li>
  </ul>


  <script>
    // 속성조작
    // 1. 클래스 속성 조작
    const h1Tag = document.querySelector('.heading')

    console.log(h1Tag)
    // <h1 class="heading">DOM 선택</h1>

    console.log(h1Tag.classList)
    // DomTokenList(1) ['heading']

    h1Tag.classList.add('red')
    // DOM 선택이 빨간색으로 변함

    h1Tag.classList.remove('red')
    // 클래스 red 사라짐

    h1Tag.classList.toggle('red')
    // 레드가 삭제된 상황이므로 클래스 추가됨



    // 2. 일반 속성 조작

    // const : 변수선언
    const aTag = document.querySelector('a')
    console.log(aTag)
    // <a href="https://www.google.com/">google</a> 

    aTag.setAttribute('href', 'https://naver.com/')
    // 속성값 네이버로 변환 -> 네이버로 감
    aTag.getAttribute('href')

    aTag.removeAttribute('href')
    aTag.getAttribute('href')   // Null

```


3. HTML 콘텐츠 조작 : 요소의 텍스트 콘텐츠를 표현 (속성값)
   - textContent : 속성값, 호출X, 콘텐츠 수정가능


### 조작 메서드
- document.createElement(tagName)
  - 작성한 tagName의 Html 요소를 생성하여 반환
  
- Node.appendChild()
  - Node = 선택한 부모
  - 한 node를 특정 부모 Node의 자식 NodeList중 마지막 자식으로 삽입
  - 추가된 Node 객체를 반환
  
- Node.removeChile()
  - Dom에서 자식 Node를 제거
  - 제거된 Node를 반환

```
  <div></div>


  <script>
    // 태그 만들기 -> 추가/삭제 가능

    // 부모 요소 선택
    const divTag = document.querySelector('div')

    // 1. 요소 생성
    const h1Tag = document.createElement('h1')

    //2. 값 추가(속성, 클래스 속성, 콘텐츠....)
    h1Tag.textContent = '제목입니다...'
    console.log(h1Tag)
    // <h1>제목입니다</h1>

    // 3. 완성한 요소를 문서에 추가
    divTag.appendChild(h1Tag)
    // 제목입니다가 div안에 담겨서 출력이 됨!

    // 4. 요소 삭제
    divTag.removeChild(h1Tag)
```

4. Style 조작
   - #### 주의사항 : CSS와 이름 사용법이 조금 달라서 확인 필요!!
     - CSS: font_size:   , JS: fontSize
   - Tag.style.color 의 형태로 접근
   - color, fontSize, borer 등 있음
   - 일반적 으로는  class(.tag)를 이용해서함!


#### NodeList
- DOM 메서드를 사용해 선택한 Node 목록
- 배열과 유사한 구조를 가짐
- index로만 각 항목에 접근가능
- 다양한 배열 메서드 사용가능
- querySelectorAll()에 반환되는 NodeList는 DOM의 변경사항을 실시간으로 반영하지 않음


#### Element
- Node의 하위유형
- element는 Dom트리에서 html요소를 나타내는 특별한 유형의 Node
- p, div, span 등의 html태그들이 element 노드를 생성
- node의 속성과 메섣를 모두 가지고 있으며 추가적인 요소 특화된 기능을 가지고 있음
- 모든 element는 node이지만 모든 node가 element인것은 아님
  
#### Dom 속성 확인 Tip
- 개발자도구 - Elements - Properties 에서 해당 요소의 모든 DOM속성 확인 가능
- MDN문서 에서 JS 속성 배우기
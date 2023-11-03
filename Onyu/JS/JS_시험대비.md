# DAY1 

<details>
<summary>접기/펼치기</summary>

- [ ] 아직 못함
- [x] 이건 함
  
----
이모지 넣기 : window + .

점선 3개 이상만 넣으면 hr 구분선 나옴
---
목차 만들기 : (내용)[#내용-띄어쓰기는-이렇게]
---
md 미리보기 : ctrl + shift + v
---

</details>




### DOM 
- 웹페이지 - 구조화된 객체로 제공 - 페이지 구조에 접근가능 - 구조, 스타일, 내용 변경 가능 / API
- 특: 모든 요소, 속성, 텍스트는 하나의 객체 + 모두 document객체의 자식임
- 조작하고자 하는 요소 "선택" + 선택된 요소 속성 "조작"
  
---
## < 클래스 속성 조작 >

### querySelector(''), querySelectorAll(' ')
- id선택 : #
- class선택 : .

### classList
- .add() : 클래스 추가
- .remove() : 클래스 제거
- .toggle() : 존재하면 제거 + return false, 아니면추가 + return true

### setAttribute(name, value)
- 지정된 요소의 속성 값 설정
- 이미 있으면 기존 값 갱신 or 새 속성 추가

### html 콘텐츠 조작
  - textContent




-----
# 10.25 함수, 객체

참조 자료형 ( Objects = Object, Array, Function )
  - 객제의 주소가 저장되는 자료형(가변, 주소가 복사)

함수는 return값이 없으면 undefined를 반환

함수정의방법 2가지
1. 선언식 : function 이라고 먼저 선언 후 시작!
2. 표현식 : const로 일름부터 정의하고 함수라고 알려줌
   - 익명함수 사용가능
   - 호이스팅 안됨 -> 함수 정의전에 먼저 사용불가

```
// 선언식
  function funcName () {
    statements
  }

// 표현식
  const funcName = function () {
    statements
  }
```



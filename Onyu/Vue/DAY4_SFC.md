# 11.07(화)

## Component
: 재사용 가능한  코드블록

특징
- UI를 독립적이고 재사용 가능한 일부분으로 분할하고 각 부분을 개별적으로 다룰 수 있음
- 자연스럽게 앱이 중첩되어 component 트리로 구성됨
- -> 내용만 다른 비슷한 툴들


## Single File Component (SFC)
컴포넌트의 템플릿(HTML), 로직(JS) 및 스타일(CSS)을 하나의 파일로 묶어낸 특수한 파일 형식 ( .vue 파일)

즉, 템플릿, 스크립트, 스타일 블록이 하나의 파일에서 합쳐짐


#### SFC 문법
- 각 vue파일은 세가지 유형의 최상위 언어블록 template, script, style으로 구성됨
- 언어블록의 작성순서는 상관X,
- 일반적으로 template-> script-> style 순서로 작성
- 각 vue파일은 template블록을 하나만 포함할 수 있음
- 
- vbase 입력 -> vbase-3-setup 선택
- 
- script setup - 한번만 쓸 수 있음, setup이 미리 선언되어있음!
  ```import { ref } from 'vue'
  const msg = ref('hello world!')
  ```
  - return 필요 X, mount 필요 X
- style태그는 여러번 사용가능


vue파일은 Vue SFC 컴파일러를 통해 컴파일 된 후 빌드되어야함

실제 프로젝트에서는 일반적으로 SFC 컴파일러를 Vite와 같은 공식 빌드도구를 사용해 사용


### Vite ( SPC build tool )
프론트엔드 개발도구 [공식문서 바로가기](https://ko.vitejs.dev/guide/)

빠른 개발환경을 위한 빌드와 개발 서버를 제공

즉, 로컬에서 빠르게 runserver 해줌


Vue로 하고자하는것 -> 하나의 폐이지에서 작업하는 것 (SPA) -> 하나의 싱글폐이지를 여러 컴포넌트로 구성할 것임! (bite를 기반으로~)


- Vue 애플리케이션 만들기 -> [공식문서 참조](https://ko.vuejs.org/guide/quick-start.html)
- nodeJS 16.0ver이상 설치 필요
- ** git bash XX, VScode terminal에서 설치 필요
- npm init vue@latest
- 나오는 질문 모두 NO!
- cd vue-project
- npm install
- npm run dev



## Node.js
server-side 실행환경


#### NPM (Node Package Manager)
Node.js의 기본 패키지 관리자 (python - pip)

영향
  - 기존에 브라우저 안에서만 동작할 수 있었던 JS를 브라우저가 아닌 서버측에서도 실행할 수 있게함
    - 프엔, 백엔 에서동일한 언러로 개발 할 수 있게 됨
  - NPM을 활용해 수많은 오픈소스 패키지와 라이브러리를 제공하여 개발자들이 손쉽게 코드를 공유하고 재사용할 수 있게 함



1. node_modules (~ venv) : 엄청 큼+무거움
   - Node.js 프로젝트에서 사용되는 외부 패키지들이 저장되는 디렉토리
   - 프로젝트 의존성 모듈을 저장하고 관리하는 공간
   - 프로젝트가 실행될 때 필요한 라이브러리와 패키지들을 포함
   - .gitignore에 작성됨

2. package-lock.json : requirements.txt같은 존재!
   - 패키지들의 실제 설치버전, 의존성관계, 하위 패키지 등을 포함하여 패키지 설치에 필요한 모든 정보를 포함
   - 패키지들의 정확한 버전을 보장하여, 여러 개발자가 협업하거나 서버 환경에서 일관성있는 의존성을 유지하는 데 도움을 줌
   - npm install 명령을 통해 패키지를 설치할 때, 명시된 버전과 의존성을 기반으로 설치

3. package.json
   - 프로젝트의 메타정보과 의존성 패키지 목록을 포함
   - 프로젝트의 이름, 버전, 작성자, 라이선스 등과 같은 메타 정보를 정의
   - package-lock 과 함께 프로젝트의 의존성 관리, 버전충돌 및 일관성 유지하는 역할
   - 요약본같은 느낌!

4. publick 디렉토리
   - 주로 다음 정적 파일을 위치시킴
     - 소스코드에서 참조되지 않는
     - 항상 같은 이름을 갖는
     - import할 필요 없는 ...
   - 항상 root 절대경로를 참조하여 참조!!
     - public/icon.png소스는 코드에서 icon.png로 쓸 수 있음


5. src 디렉토리
   - 프로젝트의 주요 소스 코드를 포함하는 곳
   - 컴포넌트, 스타일, 라우팅 등 프로젝트의 핵심 코드를 관리
  
   1. src/assets
      - 프로젝트 내에서 사용되는 자원 (이미지, 폰트, 스타일시트 등 관리)
      - 컴포넌트 자체에서 참조하는 내부파일을 저장하는 데 사용
      - 컴포넌트가 아닌 곳에서는 public디렉토리에 위치한 파일을 사용
  
    2. src/components
      - Vue 컴포넌트들을 작성하는 곳
      - App.vue -> 최상위 루트 컴포넌트!
       - 최종적으로 작성할 곳
       - 다른 모든 컴포넌트들의 부모?
  
    3. src/main.js
      - Vue인스턴스를 생성하고 앱을 초기화하는 역할
      - 필요한 라이브러리를 import 하고 전역 설정을 수행
    
 6. index.html
   - Vue앱의 기본 HTML파일
   - 앱의 진입점 (entry point)
   - Root 컴포넌트인 App.vue가 해당 페이지에 마운드(mount)됨
   - 필요한 스타일시트, 스크립트 등의 외부 리소스를 로드할 수 있음 ( ex. bootstrap CDN )


#### Module
: 프로그램을 구성하는 독립적인 코드 블록(*.js파일)

- 개발하는 앱의 크기가 커지고 복잡해지면서 파일하나에 모든 기능을 담기 어려워짐
- -> 자연스럽게 파일을 여러개로 분리하여 관리
- 이때 분리된 파일이 각각 모듈(module) 즉, js파일 하나가 하나의 모듈
- -> 모듈의 수가 많아지고 라이브러리 or 모듈간의 의존성이 깊어짐
- -> 특정곳에서 발생한 문제가 어떤 모듈간의 문제인지 파악하기 어려워짐!
- -> 복잡하고 깊은 모듈간의 의존성문제를 해결하기 위한 도구 필요
- => Bundler

#### Bundler
여러 모듈과 파일을 하나또는 여러개 의 번들로 묶어 최적화하여 앱에서 사용할 수 있게 만들어주는 도구

- 의존성관리, 코드 최적화, 리소스 관리
- 개발자가 신경쓸 필요 ㄴㄴ

컴포넌트 사용 2단계
1. 컴포넌트 파일 생성
   - MyComponent.vue 생성
   - vbase-3-setup 
2. 컴포넌트 등록
   - App 컴포넌트에 MyComponent를 등록
   - ``` import MyComponent from './components/MyComponent.vue'
    // @ : /src/ 절대경로 vue에서 미리 잡아둠
    import MyComponent from '@/components/MyComponent.vue'
    ```
3. 컴포넌트 스타일가이드
   - [공식문서 참조](https://ko.vuejs.org/style-guide/)
   - B 단계! - 가독성, 개발자 경험을 개선하기위함
   - 싱글파일 컴포넌트 파일명은 대/소문자
   - 파스칼케이스 or 케밥케이스(haha-haha) 둘중 하나만 쓰기!
   - 루트 컴포넌트 이름 (base~, App~, V~ )로 시작하기
   - 단일 인스턴스 컴포넌트 이름 (한번만 사용되는 것!) (The~ 를 붙이기)
   - 부모-자식컴포넌트 일때 자식은 부모의 이름을 앞에 두고 사용하기
   - 이름이 길더라도 약어로 쓰지않기


### Virtual DOM
가상의 DOM을 메모리에 저장하고 실제 DOM과 동기화하는 프로그래밍 개념(내부렌더링)

실제 DOM과 변경사항 비교를 통해 변경된 부분만 실제 DOM에 적용하는 방식

웹 어플리케이션의 성능을 향상시키기 위한 Vue의 내부 렌더링 기술

** 장점
- 효율성
  - 실제 DOM 조작을 최소화하고, 변경된 부분만 업데이트하여 성능을 향상
- 반응성
  - 데이터의 변경을 감지하고 Virtual DOM을 효율적으로 갱신하여 UI를 자동으로 업뎃
- 추상화
  - 개발자는 실제 DOM 조작을 Vue에게 맡기고 컴포넌트와 템플릿을 활용하는 추상화된 프로그래밍 방식으로 원하는 UI구조를 구성하고 관리할 수 있음

** 주의사항
- 실제 DOM에 접근하지 말것!!
  - JS에서 사용하느누 DOM접근 관련 메서드 사용 금지 (querySelector, addEventListener,,등)
  - ret와 Lifecycle Hooks 함수를 사용해 간접적으로 접근하여 조작할 것!
  - 
  - 조작 : input에서 ref='aaa', script에서 aaa = ref() 로 접근 가능



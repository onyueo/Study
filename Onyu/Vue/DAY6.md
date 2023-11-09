# 11.09(목)

## Router

### > Routing
네트워크에서 경로를 선택하는 프로세스

-> 웹 어플리케이션에서 다른 페이지 간의 전환과 경로를 관리하는 기술

- SSR에서의 Routing
  - 최종화면을 서버가 계속 그림!
  - 사용자가 링크를 클릭하면 계속 새로운 HTML이 필요했음

-> 서버에서 클라이언트로 옮겨짐

- CSR/SPA에서의 Routing
  - routing : 클라이언트 측에서 수행
  - JS가 새 데이터를 동적으로 가져와 전체체이지를 다시 로드하지 않음
  - 페이지는 1개이지만, 여러페이지를 사용하는 것처럼 보이도록 해야함
  - 사용자가 여러페이지를 사용하는것처럼 느끼게 만들어야함


만약 routing이 없다면
- 유저가 url 을 통한 페이지 변화를 감지할 수 없음
- 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
- URL이 1개이기 때문에 새로고침 시 처음 페이지로 돌아감
- 브라우저의 뒤로가기 기능을 사용할 수 없음
  

## [Vue Router](https://router.vuejs.org/api/)
-> CDN으로도 가져올 수 있지만 프로젝트 생성할 때 옵션으로 선택할 수 있음

```
√ Project name: ... vue-project
√ Add TypeScript? ... No / Yes
√ Add JSX Support? ... No / Yes
? Add Vue Router for Single Page Application development? » No / **Yes**
```
-> home, about 렌더링 확인~
-> App.vue 코드 변화 + router 폴더 생성 + views 폴더 생성


#### 1. RouterLink
페이지를 다시 로드하지 않고 URL을 변경하고 URL 생성 및 관련 로직을 처리

HTML의 a태그를 렌더링


#### 2. RouterView
URL에 해당하는 컴포넌트 표시

어디에나 배치하여 레이아웃을 바꿀 수 있음


#### 3. router/index.js   ~~ urls.py
라우팅에 관련된 정보 및 설정이 작성되는 곳

router에 URL과 컴포넌트를 매핑


#### 4. views
RouterView위치에 렌더링 할 컴포넌트를 배치

기존 components폴더와 기능적으로 다른것은 없으며 **단순 분류**의 의미로 구성됨

- ( 일반 컴포넌트와 구분하기 위해 컴포넌트 이름을 View로 끝나도록 작성하는 것을 권장)


---- 

### > 라우팅 기본

1. index.js에 라우터 관련 설정 작성(주소, 이름, 컴포넌트)(path, name, component)
2. RouterLink의 'to' 속성으로 index.js에서 정의한 주소 속성 값(path)사용
   
- Named Routing
  - name속성 값에 경로에 대한 이름을 지정
  - 경로를 연결하려면 RouterLink에 v-bind를 사용해 'to' prop 객체로 전달
    ```
    // 같은 의미!
      <RouterLink to="/">Home</RouterLink>
      <RouterLink :to="{ name: 'home' }">Home</RouterLink>
    ```
<br>
<br>

### Dynamic Routing Matching with Params (동적 라우팅)

매개변수를 사용한 동적 경로 매칭
  - 주어진 패턴 경로를 동일한 컴포넌트에 매핑해야 하는 경우 활용
  - 예를들어 모든 사용자의 ID를 활용하여 프로필 페이지 url을 설계한다면?
    - user/1
    - user/2  반복해야함
  - == 장고 variable routing
    ```
    <!-- index.js -->
      import UserView from '@/views/UserView.vue'
      path: '/user/:id',    // '/user/<int: id>/'

    <!-- App.vue -->
      import { ref } from 'vue'
      const userId = ref(0)

      // 나중에는 userId를 서버에서 동적으로 받아서 사용
      <RouterLink :to="{ name: 'user', params: {id: userId}}">User</RouterLink>

    <!-- UserView.vue -->
      // $ vue에서 기본적으로 제공하는 속성!! (emit 같은 거)
      // $route : 객체임
      <h2> {{ $route.params.id }} 유저의 페이지 입니다.</h2>

    ```
    - $route는 탬플릿에서 만든것 -> JS(script)에서 못씀 but, 템플릿에서 계속 계산보다는 JS에서 계산해서 넘겨주는것이 더 나음
      - JS(script)에서-> import { useRoute } from 'vue-router';
      ```
        // 템플릿
        <h2> {{ uerId }}번 유저의 페이지 입니다.</h2>

        // JS
        import { ref } from 'vue'
        import { useRoute } from 'vue-router';

        const route = useRoute()
        const uerId = ref(route.params.id)
      ```
<br>
<br>

### 프로그래밍 방식 네비게이션
router의 인스턴스 메서드를 사용해 RouterLink로 a태그를 만드는 것처럼 프로그래밍으로 네이게이션 관련 작업을 수행할 수 있음

1. 다른 위치로 이동하기
   - router.push()
  
2. 현재 위치 바꾸기
    - router.replace()


#### 1. router.push() - 뒤로가기 버튼을 눌렀을 때!! - Stack
   - 다른 url로 이동하는 메서드
   - 새 항목을 history stack에 push하므로 사용자가 브라우저 뒤로가기 버튼을 클릭하면 이전 url로 이동할 수 있음
   - RouterLink를 클릭했을 때 내부적으로 호출되는 메서드이므로 RouterLink를 클릭하는 것을 router.push()를 호출하는 것과 같음
   - 선언적 : <RouterLink : to="...">
   - 프로그래밍적 : router.push(...)

```
  <button @click="goHome">홈으로 !</button>

  
  import { useRoute, useRouter } from 'vue-router';
  // 프로그래밍 방식 네비게이션
  const router = useRouter()

  const goHome = function() {
    // router.push('/')
    router.push({ name: 'home'})
    // 위치만 바꾸고 뒤로가기 stack에 안쌓임
    // 로그인 후 뒤로가기 필요없을 경우에 사용!
    router.replace({ name: 'home'})
}

```
  - router.push({ name: 'home', params: { username: 'alice'}}) 이런식으로도 사용가능 (공식문서-navigation 참조)

#### 2. router.replace()
- push 메서드와 달리 history stack에 새로운 항목을 push하지 않고 다른 URL로 이동
- 이동전 URL로 뒤로가기 불가
- 로그인 후 뒤로가기 필요없을 경우에 사용!
 - 선언적 : <RouterLink : to="..." replace>
 - 프로그래밍적 : router.replace(...)

<br>
<br>
---

### Navigation Guard
Vue router를 통해 특정 URL에 접근할 때 다른 URL로 redirect를 하거나 취소하여 네비게이션 보호

ex) 인증 정보가 없으면 특정 페이지에 접근하지 못하게 함!

-> login required?? API???

<br>
<br>

< 종류 >

1. Globally (전역 가드)
   - 애플리케이션 전역에서 동작
   - index.js에서 정의
  
2. Per-route (라우터 가드)
  - 특정 route에서만 동작
  - index.js의 각 routes에 정의

3. In-component (컴포넌트 가드)
  - 특정 컴포넌트 내에서만 동작
  - 컴포넌트 Script에 정의


#### 1. Globally (전역 가드)
> #### router.beforeEach()

다른 URL로 이동하기 직전에 실행되는 함수 (Global Before Guards)

- router.beforeEach(to, from) => { ... return false}
- to : 이동할 URL 정보가 담긴 Route 객체
- from : 현재 URL 정보가 담긴 Route 객체
- 선택적 반환 값(return)
  - false 
    - 현재 네비게이션 취소(다음페이지로 이동 취소)
    - 브라우저 URL이 변경된 경우(사용자가 수동/ 뒤로버튼을 통해 ) from경로의 URL로 재설정
  - Route Location
    - return {name: 'About'}
    - router.push()를 호출하는 것처럼 경로 위치를 전달하여 다른 위치로 redirect
    - return이 없다면 'to' URL Route 객체로 이동


- ** 전역가드는 index.js의 router 객체에 들어있음!
  ```
  <!-- index.js router 밖에 -->
    router.beforeEach((to, from) => {
      console.log(to)
      console.log(from)
    })
  ```
- 나중에 장고랑 이을때 세션을 보냄?? 쿠키?? 
  

#### 활용 +

- login이 되어있지 않다면 페이지 진입을 막고 login페이지로 이동시키기
- 어떤 RouterLink를 클릭해도 LoginView컴포넌트만 볼 수 있음
  ```
  router.beforeEach((to, from) => {
    const isAuthenticated = false

    if (!isAuthenticated && to.name !== 'login') {
      console.log('로그인이 필요합니다')
      return { name: 'login' }
    } 
  })
  ```

> #### router.beforeEnter()
route에 진입했을 때만 실행되는 함수

- 매개변수, 쿼리 값이 변경될 때는 실행되지 않고 다른 경로에서 탐색할 때만 실행됨
- (user/1/ -> user/2/ 이렇게 바뀌는건 포함X)
- 로직은 beforeEach랑 비슷함!
- 
- 대신 router안에 path안에 넣어줌!
  ```
  <!-- index.js -->
      {
      path: '/user/:id',
      name: 'user',
      component: UserView,
      beforeEnter: (to, from) => {
        console.log(to)
        console.log(from)
      }
    },

  ```

#### 활용 +
  - 이미 로그인한 상태라면 LoginView 진입을 막고 HomeView로 이동시키기
  - (전역가드 활용 코드는 주석 처리후 진행) 
  - -> login route에 작성 필요!!
  
    ```
    {
      path: '/login',
      name: 'login',
      component: LoginView,
      beforeEnter: (to, from) => {
        if (isAuthenticated === true) {
          console.log('이미 로그인 되어있습니다')
          return { name: 'home' }
        }
      }
    },
    ```


### In-component Guard
1. onBeforeRouteLeave
2. onBeforeRouteUpdate


#### 1. onBeforeRouteLeave
- 현재 라우트에서 다른 라우트로 이동하기 전에 실행
- 사용자가 현재 페이지를 떠나는 동작에 대한 로직을 처리

스크립트 태그 내에서 작성!
```
import { onBeforeRouteLeave } from 'vue-router';

---

onBeforeRouteLeave((to, form) => {
  const answer = window.confirm('정말 떠나실 건가요?')
  if (answer === false) {
    return false
  }
})

```


#### 2. onBeforeRouteUpdate
- 이미 렌더링된 컴포넌트가 같은 라우트 내에서 업데이트되기 전에 실행
- 라우트 업데이트 시 추가적이 로직을 처리
- UserView 페이지에서 다른 id를 가진 User의 UserView 페이지로 이동하기
- user/1/ -> user/2/ 이면 url은 변경이 안되는것임
  
```
import { onBeforeRouteUpdate } from 'vue-router';


const goAnother = function() {
  router.push({ name: 'user', params: {id: 100} })
}

onBeforeRouteUpdate((to, from) => {
  userId.value = to.params.id
})
```

----
### 참고 Lazy Loading Routes
앱을 빌드할 때 페이지 로드시간이 길어지는 컴포넌트가 큰 경로를 지연되지 않고 불러오기

```component: () => import('../views/AboutView.vue')```



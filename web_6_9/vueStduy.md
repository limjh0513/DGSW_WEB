### 몇 초 후 실행

```javascript
setTimeout(function () {
  console.log("2초 뒤 실행 되었습니다");
}, 2000);
```

### 외부 라이브러리

- 링크 직접 삽입

  가능은 하지만 단점이 많음

- npm install 및 import

### 시간 다루기

new Date()가 있긴 하지만 format을 하기 불편함

Luxon 등을 추천

npm i luxon

```javascript
import { DateTime } from "luxon";

console.log(DateTime.now().toFormat("YYYY-MM-dd HH:mm:ss"));
```

### axios

1. 설치

npm i axios

2. src/main.js 파일에 추가

```javascript
import axios from "axios";

Vue.prototype.$axios = axios.crate({ imeout: 15000 });
```

3. Vue 훅 내에서 사용

   ```javascript
   this.$axios.get("url").then((resp) => {
     resp.data = "응답 본문 데이터";
   });
   ```

   ### Promise

   resolve : 요청이 성공했을 때 값 반환할 때 사용

   reject : 요청이 실패했을 때 오류 등 값 반환할 때 사용

```javascript
promise.then ((값, ...) => {

}).catch ((값, ...) => {

}).finally (() => {

})
```

    ### 	axios 옵션

​ main.js에서 axios를 생성할 때 기본 옵션 지정 가능

```
axios.create({
	timeout: 15000, //요청을 끝낼 타임아웃 ms
	baseURL: 'http://web.dgsw.kr/...' //요청 시 base 주소
	headers: {'X-Custom-...', '...'} //기본으로 포함할 헤더 정보
})
```

### 로컬 스토리지

​ 브라우저에 데이터 저장(쿠키, 세션, 로컬, indexedDB, ~~WebSQL~~(deprecated 됨))

- 항목 추가 - localStorage.setItem(키, 값)
- 항목 불러오기 - localStorage.getItem(키)
- 항목 삭제 - localStorage.removeItem(키)
- 전체 제거 - localStorage.clear()

​ JSON.stringify(a) -> 배열을 json으로 변환

​ JSON.parse("[1,2,null,4]") -> json을 배열로 변환

```javascript
let promise = new Promise(async (resolve, reject) => {
    //성공하면
    resolve(1)
    //실패하면
    reject()
})
promise.then(val => {

})
.
.

let func = async function () {
    let val = await promise
    return a
}

func.then(v => {
    v == a
})
```

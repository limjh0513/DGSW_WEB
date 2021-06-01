# Vue 디렉티브

### html 태그의 속성에 v-로 시작하는 키워드들

- v-model="변수명" : 폼 input과 textarea 에 양방향에 데이터 바인딩(폼 입력 바인딩)
- v-bind:이름 = "js 표현식" : 해당 요소나 컴포넌트에 값 전달(전달 인자)
- v-if="js 표현식", v-show="js 표현식" : 요소를 선택적으로 표시할 때 사용(조건부 렌더링)
- v-on:이름 ="함수명" or "js 표현식" : click, change 등 이벤트 발생시 실행(이벤트 핸들링)
- v-for="변수명 in 배열 or 숫자" : 요소를 배열에 매핑, 반복문으로 여러 요소 출력(리스트 렌더링)

![img](https://cdn.discordapp.com/attachments/826704810337239080/849142489767739412/unknown.png)

- title : 커서를 올렸을 때 작은 글씨를 띄움

- v-bind는 :로 축약 가능

- v-on -> @로 축약 가능

- @keypress.enter -> enter 입력 시에만 함수 호출

- computed -> 선언형 프로그램 무엇을 / 계산 해야하는 목표 데이터를 지정

  - 계산 과정의 데이터가 변경 시 다시 계산

- watch -> 명령형 프로그램 어떻게 / 감시할 데이터를 지정하고 함수 내용을 정의

  - 감시할 데이터를 지정하고 해당 데이터가 변경되면 함수 실행

npm run build -> vue를 빌드, 빌드를 다시 하면 원래 있던 빌드 폴더는 사라지고 다시 생성 됨

build 설정

```
const path = require("path");

	module.exports = {

	outputDir: path.resolve(__dirname, "../dist"),

	publicPath: "./",

	assetsDir: "static",

};
```

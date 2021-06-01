<template>
  <div>
    카카오프렌즈
    <br/>
    <input type="number" v-model="select_index" min="0" max="6" />
    <br/>
    <!-- <FriendsCard v-show="select_index != 0" v-bind:friend="friends[select_index]"></FriendsCard> -->
    <FriendsCard v-bind:friend="friends[select_index]"></FriendsCard>
    <br/><br/>
    <FriendsCard v-for="friend in friends" :key="friend.name" v-bind:friend="friend"></FriendsCard>
  </div>
</template>
<script>
import FriendsCard from '@/components/FriendsCard.vue'

export default {
  name: 'Kakao',
  components: {
    FriendsCard
      },
      data () {
        return {
          select_index: 0,
          friends: [
            {name: '어피치', image: './images/apeach.png', content: '유전자변이로 자웅동주가 된 것을 알고 복숭아 나무에서 탈출한 악동 복숭아 어피치. 섹시한 뒷태로 사람들을 매혹시키지만 성격이 매우 급하고 과격합니다.'},
            {name: '프로도', image: './images/frodo.png', content: '부자집 도시개 프로도. 잡종이라 태생에 대한 컴플렉스가 많습니다'},
            {name: '제이지', image: './images/jayg.png', content: '땅 속 나라 고향에 대한 향수병이 있는 비밀요원 제이지! 사명 의식이 투철하고, 냉철해 보이고 싶으나 어리버리합니다. 겉모습과 달리 알고 보면 외로움을 많이 타는 여린 감수성의 소유자입니다. 힙합가수 Jay-Z의 열혈팬입니다.'},
            {name: '무지', image: './images/muzi.png', content: '호기심 많은 장난꾸러기 무지! 토끼옷을 입고 있지만 정체는 단무지. 토끼옷을 벗으면 부끄러움을 많이 탑니다.'},
            {name: '네오', image: './images/neo.png', content: '새침하고 사나운 고양이 네오. 나 이외에는 중요한 게 없습니다. 자신감의 근원은 단발머리 가발에서 나옵니다.'},
            {name: '라이언', image: './images/ryan.png', content: '갈기가 없는게 콤플렉스인 수사자. 카카오프렌즈의 믿음직스러운 조언자.'},
            {name: '튜브', image: './images/tube.png', content: '겁 많고 마음 약한 오리 튜브. 극도의 공포를 느끼면 미친 오리로 변신합니다. 작은 발이 컴플렉스여서 큰 오리발을 착용합니다. 미운 오리 새끼가 먼 친척입니다.'}
          ]
        }
      }
  }
</script>

<style lang="scss" scoped>

</style>
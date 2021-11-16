<template>
    <div class="friend">
        <div><img v-bind:src="friend.image"></div>
        <div class="friend-content">
            <h3 class="friend-name">{{ friend.name }}</h3>
            <span>{{ friend.content }}</span>
        </div>
    </div>
</template>
<script>
export default {
  name: 'FriendsCard',
  props: ['friend'],
  data() {
      return {
          }
    }
}
</script>
<style lang="scss" scoped>
.friend {
	border: 1px solid #aaa;
	width: 200px;
	display: inline-block;
	vertical-align: top;
	margin: 8px;
    img {
	width: 100%;
    }
}
.friend-content {
	padding: 10px;
	border-top: 1px solid #aaa;
    h3 {
	text-align: center;
	margin: 8px 0;
    }
}

#friend-select {
	font-size: 18px;
	width: 60px;
}
</style>
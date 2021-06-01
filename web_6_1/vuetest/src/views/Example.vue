<template>
    <div>
        {{ message }}
        <button @click="buttonClicked" :title="message">클릭!</button>
        <br>
        <!-- <input type="text" v-bind:value="message" @change="onChange" @input="onInput"> -->
        <input type="text" v-model.lazy="message" @keypress="onKeyPress">
    </div>
</template>
<script>

export default {
    name: 'Example',
    data () {
        return {
            message: '안녕하세요'
        }
    },
    methods: {
        buttonClicked () {
            this.message = '반갑습니다.'
        },
        onChange(event) {
            //console.log("onChange", event.target.value);
            this.message = event.target.value
        },
        // onInput(event){
        //     console.log("onInput", event.target.value);
        // },
        onKeyPress(event){
            console.log(event.which, event.key)
        }
    },
    mounted(){
        console.log("마운트");
    }
}

</script>
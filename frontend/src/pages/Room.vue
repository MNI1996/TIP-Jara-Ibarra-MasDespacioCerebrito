<template>

   <div class="text-center">
     <h1>Welcome to the test Room</h1>
     <h2>Points {{points}}</h2>
     <template v-if="hasQuestions">
        <h1 v-if="isOver">Game finished</h1>
        <question v-else :question="questions[currentQuestion]"/>
     </template>
   </div>

</template>

<script>
import {mapGetters} from "vuex";
import io from 'socket.io-client';
import Question from "../components/Question.vue";

export default {
  name: "Room",
  data() {
    return {
      socket : io('ws://localhost:5000/rooms/'),
      roomNumber: 1,
    }
  },
  components: {Question},
  computed:{
    ...mapGetters(["questions", "points", "currentQuestion"]),
    isOver(){
      return this.currentQuestion >= this.questions.length
    },
    hasQuestions(){
      return this.questions.length > 0;
    }
  },
  created() {
    this.$store.dispatch('loadQuestions');
  },
  mounted(){
      this.createRoomConnection();
      this.joinRoom();
      this.changeBackground();
  },
  methods: {
    createRoomConnection(){
      this.socket.on('connect', () => {
        // either with send()
        this.socket.send('Hello!');
      });
    },
    joinRoom(){
      this.socket.emit('join', {room: this.roomNumber, username: "Carlos"});
    },
    changeBackground(){
      const index=document.getElementById('body')
      index.style.cssText="background-color:#DDFFAA;"
    }
  }
}
</script>

<style scoped>
body
{
  .background-color:red;
}
</style>
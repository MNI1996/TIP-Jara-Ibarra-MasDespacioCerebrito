<template>

   <div class="text-center">
     <h1>Welcome to the test Room</h1>
     <h2>Points {{points}}</h2>
     <div CLASS="row">
       <div class="col-md-4">
       </div>
       <div class="col-md-4">
         <template v-if="hasQuestions">
            <h1 v-if="isOver">Game finished</h1>
            <round v-else :question="questions[currentQuestion]"/>
         </template>
       </div>
       <div class="col-md-4">
       </div>
     </div>
   </div>

</template>

<script>
import {mapGetters} from "vuex";
import io from 'socket.io-client';
import Question from "../components/Question.vue";
import Round from "../components/Round.vue";

export default {
  name: "Room",
  data() {
    return {
      socket : io('ws://localhost:5000/rooms/'),
    }
  },
  components: {Round, Question},
  computed:{
    ...mapGetters(["questions", "points", "currentQuestion","player"]),
    ...mapGetters({roomNumber: "nextRoomId"}),
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
      this.socket.emit('join', {room: this.roomNumber, username: this.player._id});
    },
    changeBackground(){
      const index=document.getElementById('body')
      index.style.cssText="background-color:#DDFFAA;"
    }
  }
}
</script>

<style scoped>


</style>
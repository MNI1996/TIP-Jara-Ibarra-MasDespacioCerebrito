<template>
   <div class="text-center">
     <template v-if="!started">
        <h1>Welcome to the test Room</h1>
        <h2>Waiting for the owner to start the game</h2>
        <button v-if="isOwner" @click="startGame" class="btn btn-lg btn-success">Start Game</button>
     </template>
     <h2 v-if="currentRoom">Players in the room: {{currentRoom.participants}}</h2>
     <template v-if="started">
       <h2>Points {{points}}</h2>
       <div CLASS="row">
         <div class="col-md-4 offset-md-4">
           <template v-if="hasQuestions">
              <h1 v-if="isOver">Game finished</h1>
              <round v-else :question="questions[currentQuestion]"/>
           </template>
         </div>
       </div>
     </template>
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
      started: false,
    }
  },
  components: {Round, Question},
  computed:{
    ...mapGetters(["questions", "points", "currentQuestion","player", "isOwner","currentRoom"]),
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
      this.handleGameStart()
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
    },
    startGame(){
      this.socket.emit('start', {room: this.roomNumber} );
    },
    handleGameStart(){
      this.socket.on('game_started', () =>{
        console.log("EEEE YA EMPEZÓ!!!!")
        this.started = true;
      })
    }
  }
}
</script>

<style scoped>


</style>
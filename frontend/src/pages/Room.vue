<template>
   <div v-if="createdRoom" class="text-center" style="align-content: center">
     <template v-if="!started">
        <!--<h1>Welcome to the test Room</h1>-->
        <h2 id="letra">Esperando a iniciar la partida</h2>
        <button v-if="isOwner" @click="startGame" class="btn btn-lg btn-success">Start Game</button>
     </template>

     <h2 v-if="currentRoomId" id="letra">Jugadores dentro </h2>
     <div class="row">
       <div class="col-md-4">

       </div>

       <div class="col-md-4">
         <ul style="list-style: none">
           <li v-for="participant in this.currentRoom.participants">
             <user-card  :dato="participant"/>
           </li>
         </ul>
       </div>

       <div class="col-md-4">

       </div>

     </div>
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
import SimpleCard from "../components/SimpleCard.vue";
import UserCard from "../components/UserCard.vue";

export default {
  name: "Room",
  data() {
    return {
      socket : io('ws://localhost:5000/rooms/'),
      started: false,
      createdRoom: false,
    }
  },
  components: {UserCard, SimpleCard, Round, Question},
  computed:{
    ...mapGetters(["questions", "points", "currentQuestion","player", "isOwner","currentRoomId", "currentRoom"]),
    ...mapGetters({roomNumber: "nextRoomId"}),
    isOver(){
      return this.currentQuestion >= this.questions.length
    },
    hasQuestions(){
      return this.questions.length > 0;
    }
  },
  created() {
    this.$store.dispatch('loadQuestions');// se deberia cambiar a loadRoomQuestions
  },
  mounted(){
      this.createRoomConnection();
      this.joinRoom();
      this.changeBackground();
      this.handleGameStart();
      this.handleCreateRoom();
      this.handleJoinedRoom();
  },
  beforeRouteLeave (to, from, next) {
      this.socket.disconnect();
      this.$store.commit('setCurrentRoomId',null)
      next();
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
      index.style.cssText="background-color:#590995; background-image: url('Images/background tapestry.png');"
    },
    startGame(){
      this.socket.emit('start', {room: this.roomNumber} );
    },
    handleGameStart(){
      this.socket.on('game_started', () =>{
        console.log("EEEE YA EMPEZÓ!!!!")
        this.started = true;
      })
    },
    handleCreateRoom(){
      this.socket.on('created_room', async () =>{
        console.log("Se creó una nueva Room");
        await this.$store.dispatch('loadRooms');
        this.createdRoom = true;
      })
    },
    handleJoinedRoom(){
      this.socket.on('joined_room', async () =>{
        console.log("Se unió a una Room existente");
        await this.$store.dispatch('loadRooms');
        this.createdRoom = true;
      })
    }
  }
}
</script>

<style scoped>
#letra {
  color: aliceblue;
}

</style>
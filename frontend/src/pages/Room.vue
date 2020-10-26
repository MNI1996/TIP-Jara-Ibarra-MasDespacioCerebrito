<template>
   <div v-if="currentRoom" class="text-center">
     <template v-if="!started">
        <h1>Bienvenido a {{currentRoom._id}}</h1>
        <h2>Esperando que el creador {{currentRoom.owner}} empiece la partida</h2>
        <button v-if="isOwner" @click="startGame" class="btn btn-lg btn-success">Empezar Partida</button>
     </template>
     <h2 v-if="currentRoom.participants && currentRoom.participants.length >0 ">Jugadores en la Sala</h2>
     <ul>
       <li v-for="participant in this.currentRoom.participants">
         <h2>{{ participant }}</h2>
       </li>
     </ul>
     <template v-if="started">
       <h2>Puntos {{points}}</h2>
       <div class="row">
         <div class="col-md-4 offset-md-4">
           <template v-if="hasQuestions">
              <h1 v-if="isOver">Partida Terminada</h1>
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
      this.socket.emit('leave_room', {room:this.currentRoom._id, player: this.player._id});
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
      this.socket.emit('join', {room: this.currentRoom._id, username: this.player._id});
    },
    changeBackground(){
      const index=document.getElementById('body')
      index.style.cssText="background-color:#590995; background-image: url('Images/background tapestry.png');"
    },
    startGame(){
      this.socket.emit('start', {room: this.currentRoom._id} );
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
      })
    },
    handleJoinedRoom(){
      this.socket.on('joined_room', async () =>{
        console.log("Se unió a una Room existente");
        await this.$store.dispatch('loadRooms');
      })
    }
  }
}
</script>

<style scoped>


</style>
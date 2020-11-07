<template>
   <div v-if="currentRoom" class="text-center" style="align-content: center">
     <template v-if="!started">
        <h1 class="letra">Bienvenido a {{currentRoom._id}}</h1>
        <h2 class="letra">Esperando que el creador {{currentRoom.owner}} empiece la partida</h2>
        <button v-if="isOwner" @click="startGame" class="btn btn-lg btn-success">Empezar Partida</button>
     </template>

     <h2 v-if="currentRoom.participants && currentRoom.participants.length >0 " id="letra">Jugadores en la Sala</h2>
     <div class="row">
       <div class="col-md-4">

       </div>

       <div class="col-md-4" v-if="!started">
         <ul style="list-style: none">
           <li v-for="participant in this.currentRoom.participants">
             <user-card  :dato="participant"/>
           </li>
         </ul>
       </div>

       <div class="col-md-4" style="align-content: center">
         <div class="row" v-if="!started && !isOver">
           <div v-for="i in this.currentRoom.categories" class="col-md-2">
             <img :src="generateUrl(i)" alt="" style="height: 100px; width: 75px;">
           </div>
         </div>
       </div>

     </div>
     <template v-if="started">
       <h2 style="color: aliceblue">Puntos {{points}}</h2>
       <div class="row">
         <div class="col-md-4 offset-md-4">
           <template v-if="hasQuestions">
             <div v-if="isOver">
              <h1 style="color: aliceblue">Partida Terminada</h1>
              <button class="btn btn-lg btn-success" @click="toHome" >Volver al Inicio</button>
             </div>
              <round v-else :question="this.currentRoom.rounds[currentQuestion].question" :class="{show_answer: showAnswers}"/>
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
      showAnswers: false,
    }
  },
  components: {UserCard, SimpleCard, Round, Question},
  computed:{
    ...mapGetters(["questions", "points", "currentQuestion","player", "isOwner", "currentRoom"]),
    ...mapGetters({roomNumber: "nextRoomId"}),
    isOver(){
      return this.currentQuestion >= this.currentRoom.rounds_amount
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
      this.handleRoundFinished();
      this.handleRoomDeleted();
  },
  beforeRouteLeave (to, from, next) {
      this.socket.emit('leave_room', {room:this.currentRoom._id, player: this.player._id});
      this.socket.disconnect();
      this.$store.commit("resetCurrentRoom")
      next();
  },
  methods: {
    toHome(){
      this.$router.push({name: "home"})
      this.$store.dispatch("resetQuestion")
    },
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
      index.style.cssText="background-color:#790c5a; background-image: url('Images/background tapestry.png');"
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
    },
    handleRoundFinished(){
      this.socket.on('round_finished', async () =>{
        console.log("Terminó la ronda");
        this.showAnswersForRound();
      })
    },
    handleRoomDeleted(){
      this.socket.on('room_deleted', async () =>{
        console.log("Terminó la partida, el creador se fue");
        this.$noty.error("El creador se fue de la sala, te tenemos que sacar... ¡Perdón! :(", {killer: true});
        this.toHome();
      })
    },
    showAnswersForRound(){
        this.showAnswers = true;
        setTimeout(this.dispatchNextQuestion,5000);
    },
    dispatchNextQuestion(){
    this.$store.commit("nextQuestion")
    this.showAnswers = false;
    },
    generateUrl(name){
      return "Images/Categories/"+ name+".png"
    },
  }
}
</script>

<style scoped>
.letra {
  color: aliceblue;
}

</style>
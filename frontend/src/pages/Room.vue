<template>
  <div v-if="currentRoom" class="text-center" style="align-content: center">
    <template v-if="!started">
      <div class="row">
        <h1 class="letra">Bienvenido a {{ currentRoom._id }}</h1>
        <h2 class="letra">Esperando que el creador {{ currentRoom.owner }} empiece la partida</h2>
      </div>
      <div class="row">
        <div class="col-4 offset-4">
          <button v-if="isOwner" @click="startGame" class="btn btn-lg btn-success btn-block">Empezar Partida</button>
        </div>
      </div>
    </template>
    <div class="row" v-if="currentRoom.participants && currentRoom.participants.length >0 && !started">
      <div class="col-4">

      </div>
      <div class="col-4">
        <h2>Jugadores en la Sala</h2>
      </div>
      <div class="col-4">
        <h2>Categorias</h2>
      </div>
    </div>
    <div class="row justify-content-center" v-if="!started">
      <div class="col-4" v-if="again">
        <div v-for="i in this.categoriesDiff">
          <img :src="generateUrl(i)" alt="" style="height: 100px; width: 75px;">
          <p style="color: aliceblue;">{{ i }}</p>
        </div>
      </div>
      <div class="col-4">
        <ul style="list-style: none">
          <li v-for="participant in this.currentRoom.participants" style="align-items: center">
            <user-card :dato="participant"/>
          </li>
        </ul>
      </div>
      <div class="col-4" style="align-content: center">
        <div class="row" v-if="!started && !isOver">
          <div v-for="i in this.currentRoom.categories">
            <img :src="generateUrl(i)" alt="" style="height: 100px; width: 75px;" class="img-fluid">
            <p style="color: aliceblue;">{{ i }}</p>
          </div>
        </div>
      </div>
    </div>
    <template v-if="started">
      <div class="row">
        <div class="col">
          <h2 class="letra">Puntos {{ points }}</h2>
        </div>
      </div>
      <div class="row">
        <div class="col-12 col-md-6">
          <template v-if="hasQuestions">
            <div v-if="isOver">
              <h1 style="color: aliceblue">Partida Terminada</h1>
              <button class="btn btn-lg btn-success" @click="toHome">Volver al Inicio</button>
              <button class="btn btn-lg btn-success" @click="reCreate">Iniciar Otra</button>
            </div>
            <round ref="refRound" v-else :question="this.currentRoom.rounds[currentQuestion].question"
                   :class="{show_answer: showAnswers}"/>
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
      socket: io('ws://localhost:5000/rooms/'),
      started: false,
      showAnswers: false,
    }
  },
  components: {UserCard, SimpleCard, Round, Question},
  computed: {
    ...mapGetters(["questions", "points", "currentQuestion", "player", "isOwner", "currentRoom", "categories", "again"]),
    ...mapGetters({roomNumber: "nextRoomId"}),
    isOver() {
      return this.currentQuestion >= this.currentRoom.rounds_amount
    },
    hasQuestions() {
      return this.questions.length > 0;
    }
  },
  created() {
    this.$store.dispatch('loadQuestions');// se deberia cambiar a loadRoomQuestions
  },
  mounted() {
    this.createRoomConnection();
    this.joinRoom();
    this.handleGameStart();
    this.handleCreateRoom();
    this.handleJoinedRoom();
    this.handleRoundFinished();
    this.handleRoomDeleted();
    this.handleRoundStarted();
  },
  beforeRouteLeave(to, from, next) {
    this.socket.emit('leave_room', {room: this.currentRoom._id, player: this.player._id});
    this.socket.disconnect();
    this.$store.commit("resetCurrentRoom")
    next();
  },
  methods: {
    reCreate() {
      this.$router.push({name: "create_room"})
      this.$store.commit("againSet")
    },

    toHome() {
      this.$router.push({name: "home"})
      this.$store.dispatch("resetQuestion")
      this.$store.dispatch("resetPoints")
      this.$store.commit("resetAgain")
    },
    createRoomConnection() {
      this.socket.on('connect', () => {
        // either with send()
        this.socket.send('Hello!');
      });
    },
    joinRoom() {
      this.socket.emit('join', {room: this.currentRoom._id, username: this.player._id});
    },
    startGame() {
      this.socket.emit('start', {room: this.currentRoom._id});
    },
    handleGameStart() {
      this.socket.on('game_started', () => {
        this.started = true;
        this.$noty.success("¡Empieza la partida!");
        this.startRoundForOwner();
      })
    },
    handleCreateRoom() {
      this.socket.on('created_room', async () => {
        this.$noty.success("¡Se creó una nueva Sala!")
        await this.$store.dispatch('loadRooms');
      })
    },
    handleJoinedRoom() {
      this.socket.on('joined_room', async () => {
        this.$noty.success("¡Hay un nuevo jugador en la Sala!")
        await this.$store.dispatch('loadRooms');
        await this.$store.dispatch('updatePlayersInTheCurrentRoom')
      })
    },
    handleRoundFinished() {
      this.socket.on('round_finished', async () => {
        console.log("Terminó la ronda");
        this.$noty.info("¡Terminó el tiempo, mira las respuestas y concentrate para la siguiente!")
        this.showAnswersForRound();
      })
    },
    handleRoomDeleted() {
      this.socket.on('room_deleted', async () => {
        console.log("Terminó la partida, el creador se fue");
        this.$noty.error("El creador se fue de la sala, te tenemos que sacar... ¡Perdón! :(", {killer: true});
        this.toHome();
      })
    },
    handleRoundStarted() {
      this.socket.on('round_started', async () => {
        this.$noty.info("Nueva ronda! Corre el tiempo...", {killer: true});
        this.$refs.refRound.$refs.refQuestion.resetComponent()
        this.$refs.refRound.$refs.refQuestion.startRound()
      })
    },
    showAnswersForRound() {
      this.showAnswers = true;
      setTimeout(this.dispatchNextQuestion, 5000);
    },
    dispatchNextQuestion() {
      this.$store.commit("nextQuestion")
      this.showAnswers = false;
      this.$refs.refRound.$refs.refQuestion.resetComponent()
      this.$refs.refRound.$refs.refQuestion.startRound()
    },
    startRoundForOwner(){
      if(this.currentRoom.owner === this.player._id){
          this.socket.emit('round_start', {room: this.currentRoom._id});
        }
    },
    endRoundForOwner(){
        if(this.currentRoom.owner === this.player._id){
          this.socket.emit('end_round', {room: this.currentRoom._id});
        }
    },
    generateUrl(name) {
      return "Images/Categories/" + name + ".png"
    },
  }
}
</script>
<template>
  <div v-if="currentRoom" class="text-center" style="align-content: center">
    <not-started-game v-if="!started" @startGame="startGame"/>
    <template v-if="started">
      <div class="row">
        <div class="col">
          <h2 class="letra">Puntos {{ points }}</h2>
        </div>
      </div>
      <div class="row">
        <div class="col">
          <h2 class="letra">Ronda {{ currentRoundRealNumber }}</h2>
        </div>
      </div>
      <div class="row">
        <div class="col-12 col-md-6">
          <template>
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
      <game-state :game-state="gameState"/>
    </template>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import io from 'socket.io-client';
import GameState from "../components/GameState.vue";
import NotStartedGame from "../components/NotStartedGame.vue";
import Round from "../components/Round.vue";

export default {
  name: "Room",
  data() {
    return {
      socket: io('ws://localhost:5000/rooms/'),
      started: false,
      showAnswers: false,
      gameState: [],
    }
  },
  components: {NotStartedGame, Round, GameState},
  computed: {
    ...mapGetters(["questions", "points", "currentQuestion", "player", "currentRoom", "again"]),
    ...mapGetters({roomNumber: "nextRoomId"}),
    isOver() {
      return this.currentQuestion >= this.currentRoom.rounds_amount || ! this.hasQuestions;
    },
    hasQuestions() {
      return this.questions.length > 0 && this.currentRoom.rounds.length >= this.currentQuestion;
    },
    currentRoundRealNumber(){
      return this.currentQuestion +1;
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
    this.handleUpdateGameState();
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
        this.socket.emit('get_game_state', {room: this.currentRoom._id});
      })
    },
    handleUpdateGameState() {
      this.socket.on('game_state_update', async (data) => {
        console.log("Game State");
        console.log(data);
        this.gameState = data;
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
        this.socket.emit('get_game_state', {room: this.currentRoom._id});
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
  }
}
</script>
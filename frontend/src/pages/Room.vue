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
            <div v-if="gameEnded">
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
      gameEnded: false,
    }
  },
  components: {NotStartedGame, Round, GameState},
  computed: {
    ...mapGetters(["questions", "points", "currentQuestion", "player", "currentRoom", "again"]),
    ...mapGetters({roomNumber: "nextRoomId"}),
    isOver() {
      return !this.hasQuestions;
    },
    hasQuestions() {
      return this.questions.length > 0 && this.currentRoom.rounds.length >= this.currentQuestion;
    },
    lastQuestion(){
      return this.currentRoundRealNumber === this.currentRoom.rounds.length;
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
    this.handleEndGame();
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
        this.$noty.success("¡Empieza la partida!", {killer: true});
        this.startRoundForOwner();
      })
    },
    handleCreateRoom() {
      this.socket.on('created_room', async () => {
        await this.$store.dispatch('loadRooms');
      })
    },
    handleJoinedRoom() {
      this.socket.on('joined_room', async () => {
        this.$noty.success("¡Hay un nuevo jugador en la Sala!", {killer: true})
        await this.$store.dispatch('loadRooms');
        await this.$store.dispatch('updatePlayersInTheCurrentRoom')
      })
    },
    handleRoundFinished() {
      this.socket.on('round_finished', async () => {
        this.$noty.info("¡Terminó el tiempo! concentrate para la siguiente!", {killer: true})
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
        this.$noty.error("El creador se fue de la sala, te tenemos que sacar... ¡Perdón! :(", {killer: true});
        this.toHome();
      })
    },
    handleRoundStarted() {
      this.socket.on('round_started', async () => {
        this.$refs.refRound.$refs.refQuestion.resetComponent()
        this.$refs.refRound.$refs.refQuestion.startRound()
        this.socket.emit('get_game_state', {room: this.currentRoom._id});
      })
    },
    handleEndGame() {
      this.socket.on('game_ended', async () => {
        setTimeout(this.endGame, 5000);
      })
    },
    showAnswersForRound() {
      this.showAnswers = true;
      this.socket.emit('get_game_state', {room: this.currentRoom._id});
      if(!this.lastQuestion){
        setTimeout(this.dispatchNextQuestion, 5000);
      }else{
        setTimeout(this.endGame, 5000);

      }
    },
    endGame(){
      this.gameEnded = true
      this.socket.emit('get_game_state', {room: this.currentRoom._id});
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
          if(this.lastQuestion){
            this.socket.emit('end_game',{room: this.currentRoom._id});
          }
        }
    },
  }
}
</script>
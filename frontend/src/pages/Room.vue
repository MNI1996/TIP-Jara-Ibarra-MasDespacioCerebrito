<template>
  <div v-if="currentRoom" class="text-center room-game" style="align-content: center">
    <not-started-game v-if="!started && (!isOwner || (isOwner && !editing))" @startGame="startGame" @changeToPlayAgain="changeToPlayAgain"/>
    <template v-if="started">
      <div class="row round-info col-12 col-md-8 offset-md-2" v-if="!gameEnded">
        <div class="col">
          <h4>Ronda {{ currentRoundRealNumber }}</h4>
        </div>
        <div class="col">
          <h4>Tiempo: {{ countdown }}</h4>
        </div>
        <div class="col">
          <h4>Puntos {{ points }}</h4>
        </div>
      </div>

      <div class="col-12 col-md-8 offset-md-2">
        <template>
          <round ref="refRound" v-if="!gameEnded" :question="this.currentRoom.rounds[currentQuestion].question"
                 :class="{show_answer: showAnswers}"/>
        </template>
      </div>
      <div v-if="gameEnded && !playAgain">
        <div class="row col-12 col-md-10 offset-md-1 welcome">
          <img src="Images/jackpot.png" class="img-fluid welcome-logo-start">
          <h1>Partida Finalizada</h1>
          <img src="Images/jackpot.png" class="img-fluid welcome-logo-end">
        </div>
        <div class="row col-10 offset-1 col-md-10 offset-md-1 end-game-buttons">
          <button class="btn btn-lg btn-success back-to-home" @click="toHome">Volver al Inicio</button>
          <button class="btn btn-lg btn-success" v-if="isOwner" @click="updateTheRoomWithSameState">Volver a Jugar</button>
        </div>
      </div>

    </template>
    <update-room v-if="playAgain && isOwner && editing" />
    <game-state v-if="started && !playAgain" :game-state="gameState" :game-ended="gameEnded"/>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import io from 'socket.io-client';
import GameState from "../components/GameState.vue";
import NotStartedGame from "../components/NotStartedGame.vue";
import Round from "../components/Round.vue";
import UpdateRoom from "../components/UpdateRoom.vue";

export default {
  name: "Room",
  data() {
    return {
      socket: io('ws://localhost:5000/rooms/'),
      started: false,
      showAnswers: false,
      gameState: [],
      gameEnded: false,
      playAgain: false,
      currentTime: 0,
      editing: false,
    }
  },
  components: {UpdateRoom, NotStartedGame, Round, GameState},
  computed: {
    ...mapGetters(["questions", "currentQuestion", "player", "currentRoom", "again", "isOwner"]),
    ...mapGetters({roomNumber: "nextRoomId"}),
    isOver() {
      return !this.hasQuestions;
    },
    hasQuestions() {
      return this.questions.length > 0 && this.currentRoom.rounds.length >= this.currentQuestion;
    },
    lastQuestion() {
      return this.currentRoundRealNumber === this.currentRoom.rounds.length;
    },
    currentRoundRealNumber() {
      return this.currentQuestion + 1;
    },
    roundTime() {
      return this.currentRoom.round_time
    },
    countdown() {
      return this.roundTime - this.currentTime;
    },
    points() {
      if (this.gameState.length > 0) {
        return this.gameState.find(p => p.player === this.player._id)['points'];
      } else {
        return 0;
      }

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
    this.handleUpdateRoom();
  },
  beforeRouteEnter(to, from, next) {
    next(vm => {
      if (!vm.$store.getters.logged || !vm.$store.getters.currentRoom) next({name: 'home'})
    })
  },
  beforeRouteUpdate(to, from, next) {
    if (!this.$store.getters.logged || !this.$store.getters.currentRoom) next({name: 'home'})
    next()
  },
  beforeRouteLeave(to, from, next) {
    if (this.currentRoom && this.player) {
      this.socket.emit('leave_room', {room: this.currentRoom._id, player: this.player._id});
      this.socket.disconnect();
    }
    this.$store.commit("resetCurrentRoom")
    next();
  },
  methods: {
    reCreate() {
      this.$store.dispatch('resetDataRelatedToAGame')
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
      if (this.currentRoom && this.player) {
        this.socket.emit('join', {room: this.currentRoom._id, username: this.player._id});
      }
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
    handleUpdateRoom() {
      this.socket.on('room_updated', async () => {
        // this.$noty.success("¡Hay un nuevo jugador en la Sala!", {killer: true})
        await this.$store.dispatch('refreshCurrentRoom');
        this.started = false;
        this.gameEnded = false;
        this.showAnswers= false;
        this.editing = false;
        this.playAgain = false;
        this.gameState= [];
        this.currentTime= 0;
      })
    },
    showAnswersForRound() {
      this.showAnswers = true;
      this.socket.emit('get_game_state', {room: this.currentRoom._id});
      if (!this.lastQuestion) {
        setTimeout(this.dispatchNextQuestion, 5000);
      } else {
        setTimeout(this.endGame, 5000);

      }
    },
    endGame() {
      this.gameEnded = true
      this.socket.emit('get_game_state', {room: this.currentRoom._id});
    },
    dispatchNextQuestion() {
      this.$store.commit("nextQuestion")
      this.showAnswers = false;
      this.$refs.refRound.$refs.refQuestion.resetComponent()
      this.$refs.refRound.$refs.refQuestion.startRound()
    },
    startRoundForOwner() {
      if (this.currentRoom.owner === this.player._id) {
        this.socket.emit('round_start', {room: this.currentRoom._id});
      }
    },
    endRoundForOwner() {
      if (this.currentRoom.owner === this.player._id) {
        this.socket.emit('end_round', {room: this.currentRoom._id});
        if (this.lastQuestion) {
          this.socket.emit('end_game', {room: this.currentRoom._id});
        }
      }
    },
    addOne() {
      this.currentTime = this.currentTime + 1;
    },
    changeToPlayAgain(){
      this.playAgain = true;
      this.editing = true;
    },
    async updateTheRoomWithSameState() {
      await this.$store.dispatch('updateRoomWithSameState')
      this.socket.emit('update_room', {room: this.currentRoom._id});
    },
  }
}
</script>
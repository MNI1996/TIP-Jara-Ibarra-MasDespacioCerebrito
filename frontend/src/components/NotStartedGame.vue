<template>
  <div class="not-started-game-container">
    <div class="row col-12 col-md-10 offset-md-1 welcome mdc-border">
      <img src="Images/jackpot.png" class="img-fluid welcome-logo-start pulsate-fwd">
      <h1>Bienvenido a <br class="d-block d-sm-none"> {{ currentRoom._id }}</h1>
      <img src="Images/jackpot.png" class="img-fluid welcome-logo-end pulsate-fwd">
    </div>
    <div v-if="starting" class="row col-10 offset-1 col-md-4 offset-md-4 additional mdc-border starting-game-countdown">
      <div class="col-md-12">
        <h2>La partida empieza en</h2>
        <h1 class="starting-time">{{ startingTime }}</h1>
      </div>
    </div>
    <div class="row col-12 col-md-10 offset-md-1 game-information mdc-border">
      <div class="col-12 col-lg-7">
        <div class="row">
          <div class="col-12 col-md-3 game-info-div">
            <div class="row">
              <h2>Rondas</h2>
            </div>
            <div class="row">
              <h2>{{ currentRoom.rounds.length }}</h2>
            </div>
          </div>
          <div class="col-12 col-md-8 offset-md-1 game-info-div">
            <div class="row">
              <h2>Tiempo por ronda</h2>
            </div>
            <div class="row">
              <h2>{{ currentRoom.round_time }} segundos</h2>
            </div>
          </div>
        </div>
        <div class="row info-players">
          <div class="col-12 game-name">
            <h2>Jugadores en la Sala</h2>
          </div>
          <div v-if="currentRoom.participants && currentRoom.participants.length > 0" class="col-md-12 row">
            <user-card v-for="participant in currentRoom.participants" :key="participant" :dato="participant" class="col-4 col-md-2"/>
          </div>
        </div>
      </div>
      <div class="col-12 col-lg-5 info-categories-container">
        <div class="info-categories">
          <div class="col-12">
            <h2>Categorias</h2>
          </div>
          <div class="col-12">
            <div class="row flex-container padding-horizontal-mid-res">
              <div v-for="i in currentRoom.categories" class="center-card cat-card-creation">
                <p class="category-p" :class="{'no-margin-bottom': i === 'Películas y Series'}">{{ i }}</p>
                <img :src="generateUrl(i)" alt="" class="img-fluid cat-card-img">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row col-md-10 offset-md-1 additional mdc-border">
      <div class="col-md-8" :class="{'col-md-12': !isOwner}">
        <h2>Esperando que el creador {{ currentRoom.owner }} empiece la partida</h2>
      </div>
      <div class="col-md-4">
        <button v-if="isOwner" @click="$emit('changeToPlayAgain')" :disabled="starting"  class="btn btn-lg btn-success btn-block">
          Editar Partida
        </button>
        <button v-if="isOwner" @click="$emit('startGame')" :disabled="starting" class="btn btn-lg btn-success btn-block">
          Empezar Partida
        </button>
      </div>
    </div>
    <div class="row col-md-10 offset-md-1 additional mdc-border last-panel">
      <div class="col-md-12">
        <h2>¡El que responde primero gana 2 puntos!</h2>
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import UserCard from "./UserCard.vue";
import SimpleCard from "./SimpleCard.vue";

export default {
  name: "NotStartedGame",
  props: {startingTime: Number,starting: Boolean},
  computed: {
    ...mapGetters(["isOwner", "currentRoom", "categories"]),
  },
  components: {UserCard, SimpleCard},
  methods: {
    generateUrl(name) {
      return "Images/Categories/" + name + ".png"
    },
  }
}
</script>

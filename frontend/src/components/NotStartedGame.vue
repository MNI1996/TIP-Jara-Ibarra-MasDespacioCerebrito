<template>
  <div class="not-started-game-container">
    <div class="row col-12 col-md-10 offset-md-1 welcome">
      <img src="Images/jackpot.png" class="img-fluid welcome-logo-start">
      <h1>Bienvenido a <br class="d-block d-sm-none"> {{ currentRoom._id }}</h1>
      <img src="Images/jackpot.png" class="img-fluid welcome-logo-end">
    </div>
    <div class="row col-12 col-md-10 offset-md-1 game-information">
      <div class="col-12 col-md-7">
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
              <h2>{{ 10 }}</h2>
            </div>
          </div>
        </div>
        <div class="row info-players">
          <div class="col-12 game-name">
            <h2>Jugadores en la Sala</h2>
          </div>
          <div v-if="currentRoom.participants && currentRoom.participants.length > 0" class="col-md-12 row">
            <user-card v-for="participant in this.currentRoom.participants" :dato="participant" class="col-4 col-md-2"/>
          </div>
        </div>
      </div>
      <div class="col-12 col-md-5 info-categories-container">
        <div class="info-categories">
          <div class="col-12">
            <h2>Categorias</h2>
          </div>
          <div class="col-12" style="align-content: center">
            <div class="row">
              <div v-for="i in this.currentRoom.categories" class="col-4 col-md-3 center-card cat-card-creation">
                <p>{{ i }}</p>
                <img :src="generateUrl(i)" alt="" class="img-fluid cat-card-img">
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row col-md-10 offset-md-1 additional">
      <div class="col-md-8" :class="{'col-md-12': !isOwner}">
        <h2>Esperando que el creador {{ currentRoom.owner }} empiece la partida</h2>
      </div>
      <div class="col-md-4">
        <button v-if="isOwner" @click="$emit('startGame')" class="btn btn-lg btn-success btn-block">
          Empezar Partida
        </button>
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
  props: {},
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

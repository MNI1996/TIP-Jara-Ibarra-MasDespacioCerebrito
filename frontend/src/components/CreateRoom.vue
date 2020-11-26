<template>
  <div class="not-started-game-container">
    <div class="row col-12 col-md-10 offset-md-1 welcome">
      <img src="Images/jackpot.png" class="img-fluid welcome-logo-start">
      <div class="col-md-5">
        <h1>Nombre de la sala:</h1>
      </div>
      <div class="col-md-5 input-div-room-name">
        <input type="text" v-model="roomName" class="input-group"/>
      </div>
      <img src="Images/jackpot.png" class="img-fluid welcome-logo-end">
    </div>
    <div class="row col-12 col-md-10 offset-md-1 game-creation">
      <div class="col-md-12">
        <div class="row">
          <div class="col-12 col-md-3 game-info-div">
            <div class="row rondas-div">
              <h2>Rondas</h2>
            </div>
            <div class="row">
              <select name="rondas" v-model="rounds">
                <option selected value="5">5</option>
                <option value="6">6</option>
                <option value="7">7</option>
                <option value="8">8</option>
                <option value="9">9</option>
                <option value="10">10</option>
              </select>
            </div>
          </div>
          <div class="col-12 col-md-8 offset-md-1 game-info-div">
            <div class="row">
              <h2>Definir tiempo por ronda</h2>
            </div>
            <div class="row">
              <select name="dificultad" v-model="dificultad">
                <option selected value="1">Facil</option>
                <option value="2">Media</option>
                <option value="3">Dificil</option>
              </select>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-12 categories-creation ">
        <div class="col-12">
          <h2 class="select-category">Seleccionar Categorias</h2>
        </div>
        <div class="col-12" style="align-content: center">
          <div class="row">
            <simple-card v-for="i in categories" :dato="i" @addCategory="addCategory"/>
          </div>
        </div>
      </div>
    </div>
    <div class="row col-md-10 offset-md-1 additional">
      <div class="col-md-4">
        <button @click="createARoom" class="btn btn-lg btn-success btn-block">Crear Sala</button>
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import SimpleCard from "./SimpleCard.vue";

export default {
  name: "CreateRoom",
  components: {SimpleCard},
  data() {
    return {
      roomName: "",
      roomCategories: [],
      rounds: 5,
      dificultad: 1,
    }
  },
  computed: {
    ...mapGetters(["categories", "currentRoom", "again"]),
  },
  methods: {
    categoriesDiff() {
      let cat = this.categories.filter(x => !this.currentRoom.roomCategories.includes(x))
      return cat
    },
    addCategory(categorie) {
      let cond = this.roomCategories.includes(categorie)
      if (!cond) {
        this.roomCategories = this.roomCategories.concat(categorie)
        //tendria que actualizar la lista de las categorias sin categorie y redibujar
        //seria asi
        // this.categories=this.categories.filter(e=> e!==categorie)
      } else {
        this.roomCategories = this.roomCategories.filter(e => e !== categorie)
        //tendria que actualizar la lista de categories con categorie y redibujar
        //seria asi
        // this.categories=this.categories.concat(categorie)
      }
    },
    updatedCats() {

    },
    async createARoom() {
      await this.$store.dispatch('createRoom', {
        name: this.roomName,
        categories: this.roomCategories,
        rounds: this.rounds
      })
      if (this.currentRoom) {
        this.$router.push({name: "room"})
      }
    },

  }
}
</script>


<style scoped>


</style>
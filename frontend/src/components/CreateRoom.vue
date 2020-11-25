<template>
  <div>
    <div class="justify-content-center " style="margin-top: 1%;">
      <div class="row">
        <div class="col-12 col-md-6">
          <h1>Nombre de la Sala: </h1>
        </div>
        <div class="col-12 col-md-6">
          <input type="text" v-model="roomName" class="input-group"/>
        </div>
      </div>
      <div class="row">
        <div class="col-12 col-md-3 row">
          <div class="col-6">
            <h3>Rondas</h3>
          </div>
          <div class="col-6">
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
        <div class="col-12 col-md-3 row">
          <div class="col-6">
            <h3>Dificultad</h3>
          </div>
          <div class="col-6">
            <select name="dificultad" v-model="dificultad">
              <option selected value="1">Facil</option>
              <option value="2">Media</option>
              <option value="3">Dificil</option>
            </select>
          </div>
        </div>
        <div class="col-12 col-md-3">
          <button @click="createARoom" class="btn btn-lg btn-success">Crear Sala</button>
        </div>
      </div>
    </div>
    <div class="row">
      <h1> Elija las categorias</h1>
    </div>
    <div class="row justify-content-center">
      <div class="col-12 row">
        <simple-card v-for="i in categories" :dato="i" @addCategory="addCategory"/>
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
<template>
  <div class="not-started-game-container">
    <div class="row col-12 col-md-10 offset-md-1 welcome">
      <img src="Images/jackpot.png" class="img-fluid welcome-logo-start pulsate-fwd">
      <div class="col-md-5">
        <h1>Nombre de la sala:</h1>
      </div>
      <div class="col-md-5">
        <h1>{{this.currentRoom._id}}</h1>
      </div>
      <img src="Images/jackpot.png" class="img-fluid welcome-logo-end pulsate-fwd">
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
                <option v-for="n in [5,6,7,8,9,10]" :value=n>{{n}}</option>
              </select>
            </div>
          </div>
          <div class="col-12 col-md-8 offset-md-1 game-info-div">
            <div class="row">
              <h2>Definir tiempo por ronda</h2>
            </div>
            <div class="row">
              <select name="time" v-model="time">
                <option v-for="n in [10,15,30,45,60]" :value=n>{{n}} segundos</option>
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
            <simple-card v-for="i in categories" :key="i" :dato="i" @addCategory="addCategory"/>
          </div>
        </div>
      </div>
    </div>
    <div class="row col-md-10 offset-md-1 additional">
      <div class="col-md-4">
        <button @click="updateRoom" class="btn btn-lg btn-success btn-block">Actualizar Sala</button>
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import SimpleCard from "./SimpleCard.vue";

export default {
  name: "UpdateRoom",
  components: {SimpleCard},
  data() {
    return {
      roomName: "",
      roomCategories: [],
      rounds: 5,
      time: 10,
    }
  },
  computed: {
    ...mapGetters(["categories", "currentRoom", "again"]),
  },
  mounted(){
    this.rounds = this.currentRoom.rounds_amount;
    this.time = this.currentRoom.round_time;
    this.roomCategories = this.currentRoom.categories;

  },
  methods: {
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
    async updateRoom() {
      await this.$store.dispatch('updateRoom', {
        categories: this.roomCategories,
        rounds: this.rounds,
        round_time: this.time,
      })
      this.$parent.socket.emit('update_room', {room: this.currentRoom._id});
    },
  },
  beforeRouteEnter(to, from, next) {
      next(vm => {
        // access to component instance via `vm`
        if(!vm.$store.getters.logged) next({name:'home'})
      })
    },
    beforeRouteUpdate(to, from, next) {
        if(!this.$store.getters.logged) next({name:'home'})
        next()
    },
}
</script>
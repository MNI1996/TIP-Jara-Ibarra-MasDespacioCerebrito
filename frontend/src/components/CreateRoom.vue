<template>
    <div>
      <template>
        <div class="row justify-content-center " style="margin-top: 1%;">
          <div class="col">
            <h1>Nombre de la Sala: </h1>
          </div>
          <div class="col">
            <div class="row">
              <input type="text" v-model="roomName"  class="input-group"/>
            </div>
            <div class="row">
              <div class="col-4">
                <h3>Rondas</h3>
                <select name="rondas"  v-model="rounds">
                  <option selected value="5">5</option>
                  <option value="6">6</option>
                  <option value="7">7</option>
                  <option value="8">8</option>
                  <option value="9">9</option>
                  <option value="10">10</option>
                </select>
              </div>
              <div class="col-4">
                <h3>Dificultad</h3>
                <select name="dificultad" v-model="dificultad">
                  <option selected value="1" >Facil</option>
                  <option value="2">Media</option>
                  <option value="3">Dificil</option>
                </select>
              </div>
            </div>
          </div>
          <div class="col">
            <button @click="createARoom" class="btn btn-lg btn-success">Crear Sala</button>
          </div>
        </div>
        <div class="row">
          <h1 > Elija las categorias</h1>
        </div>
        <div class="row justify-content-center" v-if="again">
          <div class="col-6" >
            <h3> Agregable:</h3>
            <ul>
              <li v-for="i in categoriesDiff">
                <simple-card :dato="i" @addCategory="addCategory"/>
              </li>
            </ul>
          </div>
          <div class="col-6">
            <h3> Agregado:</h3>
            <ul>
              <li v-for="i in this.currentRoom.categories" style="align-content: center" > <simple-card :dato="i" @addCategory="addCategory"/></li>
            </ul><!--this.currentRoom.categories da null por que se resetea currenRoom al cambiar de ruta -->
          </div>
        </div>
        <div class="row justify-content-center" v-else>
          <div class="col-6">
            <h3> Agregable:</h3>
            <ul>
              <li v-for="i in categories">
                <simple-card :dato="i" @addCategory="addCategory"/>
              </li>
            </ul>
          </div>
          <div class="col-6">
            <h3> Agregado:</h3>
            <ul>
              <li v-for="i in roomCategories" style="align-content: center" > <simple-card :dato="i" @addCategory="addCategory"/></li>
            </ul>

          </div>
        </div>
      </template>
    </div>

</template>

<script>
import {mapGetters} from "vuex";
import SimpleCard from "./SimpleCard.vue";

export default {
  name: "CreateRoom",
  components: {SimpleCard},
    data(){
    return {roomName: "",
            roomCategories: [],
            rounds:5,
            dificultad:1,
            }
  },
  computed:{
    ...mapGetters(["categories", "currentRoom","again"]),
  },
  methods:{
    categoriesDiff(){
      let cat= this.categories.filter(x => !this.currentRoom.roomCategories.includes(x))
      return cat
    },
    addCategory(categorie){
      let cond= this.roomCategories.includes(categorie)
      if (!cond) {
       this.roomCategories= this.roomCategories.concat(categorie)
        //tendria que actualizar la lista de las categorias sin categorie y redibujar
        //seria asi
        // this.categories=this.categories.filter(e=> e!==categorie)
      }
      else {
        this.roomCategories= this.roomCategories.filter(e => e !== categorie)
        //tendria que actualizar la lista de categories con categorie y redibujar
        //seria asi
        // this.categories=this.categories.concat(categorie)
      }
    },
    updatedCats(){

    },
    async createARoom(){
      await this.$store.dispatch('createRoom', {name: this.roomName, categories: this.roomCategories,rounds:this.rounds})
      if(this.currentRoom){
          this.$router.push({name: "room"})
      }
    },

  }
}
</script>


<style scoped>


</style>
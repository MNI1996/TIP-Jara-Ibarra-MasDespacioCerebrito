<template>
  <div>
   <!-- <div v-if="again">
      <template>
        <div class="row justify-content-center " style="margin-top: 1%;">
          <div class="col">
            <h1>Nombre de la Sala: </h1>
          </div>
          <div class="col">
            <input type="text" v-model="roomName"  class="input-group" />
          </div>
          <div class="col">
            <button @click="createARoom" class="btn btn-lg btn-success">Crear Sala</button>
          </div>
        </div>
        <div class="row">
          <h1 > Elija las categorias</h1>
        </div>
        <div class="row justify-content-center">
          <div class="col-6">
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
            </ul>
          </div>
        </div>
      </template>
    </div>-->
    <div>
      <template>
        <div class="row justify-content-center " style="margin-top: 1%;">
          <div class="col">
            <h1>Nombre de la Sala: </h1>
          </div>
          <div class="col">
            <input type="text" v-model="roomName"  class="input-group"/>
          </div>
          <div class="col">
            <button @click="createARoom" class="btn btn-lg btn-success">Crear Sala</button>
          </div>
        </div>
        <div class="row">
          <h1 > Elija las categorias</h1>
        </div>
        <div class="row justify-content-center">
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
      await this.$store.dispatch('createRoom', {name: this.roomName, categories: this.roomCategories})
      if(this.currentRoom){
          this.$router.push({name: "room"})
      }
    },

  }
}
</script>


<style scoped>


</style>
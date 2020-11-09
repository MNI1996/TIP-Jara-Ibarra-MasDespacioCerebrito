<template>
  <div>
    <div class="row">
      <div class="col-6">
        <h1>Nombre de la Sala: </h1>
        <input type="text" v-model="roomName" />
      </div>
      <div class="col-6">
        <button @click="createARoom" class="btn btn-lg btn-success">Create a Room</button>
      </div>
    </div>
    <div class="row">
      <h1 > Elija las categorias</h1>
    </div>
    <div class="row justify-content-center">
      <div class="col-6">
        <h3> Agregable</h3>
        <ul>
          <li v-for="i in catAux">
            <simple-card :dato="i" @addCategory="addCategory"/><!-- averiguar si existe un remount de div -->
          </li>
        </ul>
      </div>
      <div class="col-6">
        <h3> Se agregó:</h3>
        <ul>
          <li v-for="i in roomCategories" style="align-content: center" > <simple-card :dato="i" @addCategory="addCategory"/></li>
        </ul>
      </div>
       <div class="col-md-4">

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
    data(){
    return {roomName: "",
            roomCategories: [],
            }
  },
  computed:{
    ...mapGetters(["categories", "currentRoom"]),
  },
  methods:{
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
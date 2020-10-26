<template>
  <div>
    <h1>Nombre de la Sala: </h1>
    <input type="text" v-model="roomName" />
    <h1 style="color: aliceblue"> Elija las categorias</h1>
    <div class="row">
      <ul>
        <li v-for="i in categories">
          <simple-card :dato="i" @addCategory="addCategory"/>
        </li>
      </ul>
    </div>
    <div class="row">
      <div class="col-md-4">
        <h3> Se agregó:</h3>
      </div>
      <div class="col-md-4" >
        <ul>
          <li v-for="i in roomCategories" style="align-content: center" > <h4>{{ i }}</h4></li>
        </ul>
      </div>
       <div class="col-md-4">
        <button @click="createARoom" class="btn btn-lg btn-success">Create a Room</button>
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
            roomCategories: []}
  },
  computed:{
    ...mapGetters(["categories"]),
  },
  methods:{
    addCategory(categorie){
      let cond= this.roomCategories.includes(categorie)
      if (!cond) {
       this.roomCategories= this.roomCategories.concat(categorie)
      }
    },
    async createARoom(){
      await this.$store.dispatch('createRoom', {name: this.roomName, categories: this.roomCategories})
      this.$router.push({name: "room"})
    },

  }
}
</script>


<style scoped>
ul {
  list-style-type: none;
}

li {
  float: left;
  margin: 15px;
  list-style: none;
 }

</style>
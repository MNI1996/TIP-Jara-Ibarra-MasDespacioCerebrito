<template>
  <div>
    <h1 style="color: aliceblue"> Elija las categorias</h1>
    <div class="row">
      <ul>
        <li v-for="i in categories">
          <simple-card :dato="i"/>
        </li>
      </ul>
    </div>


    <!--<div class="row">
     <div class="col-md-4">
     </div>
     <div class="col-md-4">
       <div style="text-align: center" v-for="i in categories">
         <h1>
           {{i}}
         </h1>
       </div>
     </div>
   </div>

  <div v-for="group in gemerateSublist(categories,3)">
     <div v-for="cat in group" class="row">
       <div class="col" >
         <h1>{{ cat }}</h1>
       </div>
     </div>
   </div>-->

    <button @click="createARoom" class="btn btn-lg btn-success">Create a Room</button>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import SimpleCard from "./SimpleCard.vue";

export default {
  name: "CreateRoom",
  components: {SimpleCard},
  computed:{
    ...mapGetters(["categories"]),
  },
  /*data(){
    return{
      cats:[],
    }
  },*/
  methods:{
    createARoom(){
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
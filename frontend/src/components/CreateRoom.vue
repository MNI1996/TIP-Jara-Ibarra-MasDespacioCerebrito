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
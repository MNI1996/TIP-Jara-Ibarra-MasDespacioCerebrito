<template>
  <div class="text-center">
    <user-login v-if="!player"/>
    <rooms/>
    <button @click="goToRoom" class="btn btn-lg btn-success">Play!</button>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import Rooms from "./Rooms.vue";
import UserLogin from "../components/UserLogin.vue";

export default {
  name: "Home",
  components: {Rooms, UserLogin},
  computed:{
    ...mapGetters(["questions","player"]),
  },


  mounted(){
    this.changeBackground();
  },

  methods:{
    goToRoom(){
      this.$router.push({name:"room"})
    },
    changeBackground(){
      var index=document.getElementById('body')
      index.style.cssText="background-color:#000000;"
    }
  }
}
</script>

<style scoped>
.boton div
{
  display: block;
}
.boton div:hover
{
  background-color:#666
}
.options div
{
  background-color: aqua;
}
.btn-block:hover{
  background-color: coral;
}
</style>
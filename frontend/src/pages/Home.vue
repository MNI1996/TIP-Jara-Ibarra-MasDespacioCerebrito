<template>
  <div class="text-center, row" id="margen">
    <div class="col-md-2" >
      <user-login v-if="!player"/>
      <button @click="goToRoom" class="btn btn-lg btn-success">Play!</button>
    </div>
    <div class="col-md-8" >
      <rooms/>
    </div>

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
#margen div
{
  margin-top: 50px;
}
</style>
<template>
  <div class="text-center, row" id="margen">

      <user-login v-if="!player"/>
      <rooms v-if="logged"/>
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
    ...mapGetters(["player","logged"]),
  },


  mounted(){
    this.changeBackground();
  },

  methods:{
    changeBackground(){
      var index=document.getElementById('body')
      index.style.cssText="background-color:#1aa6b7;background-image: url('Images/background tapestry.png');"
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
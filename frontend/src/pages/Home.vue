<template>
  <div class="text-center, row" id="margen">
    <div class="col-md-2" >
      <user-login v-if="!player"/>
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
    ...mapGetters(["player"]),
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
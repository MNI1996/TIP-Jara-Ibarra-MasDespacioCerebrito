<template>
  <div class="text-center">
    <button @click="goToRoom" class="btn btn-lg btn-success">Play!</button>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "Home",
  computed:{
    ...mapGetters(["questions"]),
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
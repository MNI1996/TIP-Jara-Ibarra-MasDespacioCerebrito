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
  methods:{
    goToRoom(){
      this.$router.push({name:"room"})
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
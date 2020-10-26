<template>
  <div class="row"  >

    <div class="col">
      <h4>ID: {{room._id}}</h4>
    </div>
    <div class="col">
      <h4>Creador: {{this.room["owner"]}}</h4>
    </div>
    <div class="col">
      <h4>Jugadores: {{this.room["participants"].length+1}}</h4>
    </div>
    <div class="col">
      <button @click="goToRoom" class="btn btn-lg btn-success">Unirse a sala!</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "RoomCard",
  props:{
    room: Object,
  },
  methods:{
    async goToRoom(){
      await this.$store.dispatch("getRoom", this.room._id)
      this.$router.push({name: "room"})
    }
  }
}
</script>

<style scoped>

</style>
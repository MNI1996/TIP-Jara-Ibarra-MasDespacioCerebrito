<template>
  <div class="row"  >

    <div class="col">
      <h4>ID: {{room._id}}</h4>
    </div>
    <div class="col">
      <h4>Creador: {{room.owner}}</h4>
    </div>
    <div class="col">
      <h4>Participantes: {{room.participants.length}}</h4>
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
    goToRoom(){
      this.$store.commit("setCurrentRoomId", this.room._id)
      this.$router.push({name: "room"})
    }
  }
}
</script>

<style scoped>
/*style="border-style: inset;border-color: rgba(255,255,255,0.5);*/
</style>
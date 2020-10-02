<template>
  <div class="row" style="border-style: inset;border-color: rgba(255,255,255,0.5);" >

    <div class="col">
      <h4>ID: {{room._id}}</h4>
    </div>
    <div class="col">
      <h4>Owner: {{room.owner}}</h4>
    </div>
    <div class="col">
      <h4>Participants: {{room.participants.size}}</h4>
    </div>
    <div class="col">
      <button @click="goToRoom" class="btn btn-lg btn-success">Join Room</button>
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

</style>
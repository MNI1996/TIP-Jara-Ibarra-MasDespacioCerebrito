<template>
  <div style="border-style: inset;border-color: aqua;">
    <h1>ID: {{room._id}}</h1>
    <h2>Owner: {{room.owner}}</h2>
    <h2>Participants: {{room.participants}}</h2>
    <button @click="goToRoom" class="btn btn-lg btn-success">Join Room</button>
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
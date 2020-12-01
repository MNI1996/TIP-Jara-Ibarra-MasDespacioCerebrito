<template>
  <div class="row player-info-card">
    <div class="ranking-points col col-md-3"><h3>{{ room._id }}</h3></div>
    <div class="ranking-points col col-md-3"><h3>{{ this.room["owner"] }}</h3></div>
    <div class="ranking-points col col-md-3"><h3>{{ this.room["participants"].length }}</h3></div>
    <div class="ranking-points col col-md-2">
      <button @click="goToRoom" class="btn btn-success">Unirse</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "RoomCard",
  props: {
    room: Object,
  },
  methods: {
    async goToRoom() {
      await this.$store.dispatch("joinIt", this.room._id)
      this.$router.push({name: "room"})
    }
  }
}
</script>

<style scoped>

</style>
<template>
  <div class="row">
    <div class="col-11 room-card">
      <div class="row">
        <div class="ranking-points col col-md-5"><h3>{{ room._id }}</h3></div>
        <div class="ranking-points col col-md-2"><h3>{{ this.room["owner"] }}</h3></div>
        <div class="ranking-points col col-md-3"><h3>{{ this.room["participants"].length }}</h3></div>
        <div class="ranking-points col col-md-1">
          <button @click="goToRoom" class="btn btn-success">Unirse</button>
        </div>
      </div>
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
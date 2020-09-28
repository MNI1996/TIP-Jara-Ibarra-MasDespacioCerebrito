<template>
  <div>
    <template v-if="rooms.length > 0">
      <h1>Those are all the rooms available now</h1>
      <room-card v-for="room in rooms" />
    </template>
    <template v-else>
      <h1>There are no rooms created right now</h1>
    </template>
    <button @click="goToCreateARoom" class="btn btn-lg btn-success">Create a Room</button>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import RoomCard from "../components/RoomCard.vue";

export default {
name: "Rooms",
  components:{
    RoomCard
  },
  computed:{
    ...mapGetters(["rooms"]),
  },
  methods:{
    goToCreateARoom(){
     this.$router.push({name: "create_room"})
    }
  }
}
</script>

<style scoped>

</style>
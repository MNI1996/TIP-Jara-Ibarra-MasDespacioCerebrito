<template>

  <div>
    <template v-if="rooms.length > 0">
      <ul>
        <li v-for="room in rooms" id="fondo">
          <div>
            <room-card :room="room" />
          </div>
        </li>
      </ul>
      <!-- <h1>Those are all the rooms available now</h1>-->
      <button @click="goToCreateARoom" class="btn btn-lg btn-success">Create a Room</button>
    </template>
    <template v-else>
      <h1>There are no rooms created right now</h1>
      <button @click="goToCreateARoom" class="btn btn-lg btn-success">Create a Room</button>
    </template>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import RoomCard from "../components/RoomCard.vue";

export default {
name: "Rooms",


computed:{
  ...mapGetters(["rooms", "nextRoomId"]),
},
  methods: {
    createRoomConnection() {
      this.socket.on('connect', () => {
        // either with send()
        this.socket.send('Hello!');

        // or with emit() and custom event names
        this.socket.emit('my_event', 'Hello!');
      })
    },
    goToCreateARoom() {
      this.$store.commit('setCurrentRoomId',this.nextRoomId);
      this.$router.push({name: "create_room"})
    },
  },
  components:{
    RoomCard
  },

  mounted() {
    this.$store.dispatch("loadRooms");
  }

}

</script>

<style scoped>
#fondo div:hover
{
  background-color: darkcyan;

}
</style>
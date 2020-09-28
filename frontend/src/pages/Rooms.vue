<template>
<<<<<<< HEAD
  <h1>This is rooms</h1>
  <ul >
    <li v-for="room in rooms">
      <div class="row">
        <div class="col-md-8">
      <h3>
        {{room.name}}
      </h3>
        </div>
        <div class="col-md-4">
          <button @click="methods.createRoomConnection()" class="btn btn-lg btn-success">Entrar a la sala</button>
        </div>
      </div>
    </li>
  </ul>
=======
  <div>
    <template v-if="rooms.length > 0">
      <h1>Those are all the rooms available now</h1>
      <room-card v-for="room in rooms" :room="room" />
    </template>
    <template v-else>
      <h1>There are no rooms created right now</h1>
    </template>
    <button @click="goToCreateARoom" class="btn btn-lg btn-success">Create a Room</button>
  </div>
>>>>>>> 3664a4eee36d9a6b0eb266c139908a23b3821715
</template>

<script>
import {mapGetters} from "vuex";
import RoomCard from "../components/RoomCard.vue";

export default {
name: "Rooms",
<<<<<<< HEAD

computed:{
  methods: {
    createRoomConnection(){
      this.socket.on('connect', () => {
        // either with send()
        this.socket.send('Hello!');

        // or with emit() and custom event names
        this.socket.emit('my_event', 'Hello!');
      });
=======
  components:{
    RoomCard
  },
  computed:{
    ...mapGetters(["rooms"]),
  },
  mounted() {
    this.$store.dispatch("loadRooms");
  },
  methods:{
    goToCreateARoom(){
     this.$router.push({name: "create_room"})
>>>>>>> 3664a4eee36d9a6b0eb266c139908a23b3821715
    }
  }
}
}

</script>

<style scoped>

</style>
<template>
  <div v-if="searchedRoom!==null">
    <div style="margin-bottom: 20px ;align-content: center">
      <input  v-model="id" type="text" size="80">
      <button @click="searchRoom" class="btn btn-lg btn-success">Buscar sala</button>
    </div>
    <room-card :room="searchedRoom"/>
    <button @click="goBacK" class="btn btn-lg btn-success">Volver a Salas</button>
  </div>

  <div v-else>
    <template v-if="rooms.length > 0">
      <div style="margin-bottom: 20px ;align-content: center">
          <input  v-model="id" type="text" size="60">
          <button @click="searchRoom" class="btn btn-lg btn-success">Buscar sala</button>
      </div>
      <ul>
        <li v-for="room in rooms" id="fondo">
            <room-card :room="room" />
        </li>
      </ul>
      <!-- <h1>Those are all the rooms available now</h1>-->
      <button @click="goToCreateARoom" class="btn btn-lg btn-success">Crear sala</button>
    </template>
    <template v-else>
      <h1>No hay salas en este momento</h1>
      <button @click="goToCreateARoom" class="btn btn-lg btn-success">Crear sala</button>
    </template>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import RoomCard from "../components/RoomCard.vue";

export default {
name: "Rooms",

  data() {
    return {
      id:null,
    }
  },
computed:{
  ...mapGetters(["rooms", "nextRoomId", "searchedRoom"]),
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
    goBacK(){
      this.$store.dispatch("resetSearch")
      this.id=null
    },
    goToCreateARoom() {
      this.$store.commit('setCurrentRoomId',this.nextRoomId);
      this.$router.push({name: "create_room"})
    },
    searchRoom(){
      this.$store.dispatch("getRoom",this.id)
    }
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
  background-color: rgba(61,126,166,0.5);
  border-radius: 15px;
}
li {list-style:none;}
</style>
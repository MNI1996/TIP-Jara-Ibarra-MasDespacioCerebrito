<template>
  <div>
    <div class="welcome" v-if="searchedRooms.length > 0  || rooms.length > 0">
      <div>
        <input class="styleInput" v-model="id" type="text">
        <button @click="searchRoom" class="btn btn-lg btn-success">Buscar sala</button>
        <button @click="goToCreateARoom" class="btn btn-lg btn-success">Crear sala</button>
      </div>
      <div id="rooms-table">
        <div class="row justify-content-center">
          <div class=" col col-md-3"><h3><strong>Nombre</strong></h3></div>
          <div class=" col col-md-3"><h3><strong>Creador</strong></h3></div>
          <div class=" col col-md-3"><h3><strong>Jugadores</strong></h3></div>
          <div class=" col col-md-2"></div>
        </div>
        <room-card v-if="searchedRooms.length > 0" v-for="room in searchedRooms" :room="room"/>
        <room-card v-if="!searchedRooms.length > 0" v-for="room in rooms" :room="room"/>
      </div>
      <button @click="goBacK" class="btn btn-lg btn-success">Limpiar busqueda</button>
      <button @click="loadRooms" class="btn btn-lg btn-success">Recargar Salas</button>
    </div>
    <template v-else>
      <div class="row col-md-10 offset-md-1 additional">
        <div class="col-md-12">
          <h1 class="no-rooms-title">No hay salas en este momento</h1>
        </div>
        <div class="col-6">
          <button @click="goToCreateARoom" class="btn btn-lg btn-success btn-block">Crear sala</button>
        </div>
        <div class="col-6">
          <button @click="loadRooms" class="btn btn-lg btn-success btn-block">Recargar Salas</button>
        </div>
      </div>
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
      id: null,
    }
  },
  computed: {
    ...mapGetters(["rooms", "nextRoomId", "searchedRooms"]),
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
    goBacK() {
      this.$store.dispatch("resetSearch")
      this.id = null
    },
    goToCreateARoom() {
      this.$store.commit('setCurrentRoomId', this.nextRoomId);
      this.$router.push({name: "create_room"})
    },
    searchRoom() {
      this.$store.dispatch("getSearchedRooms", this.id)
    },
    loadRooms() {
      this.$store.dispatch("loadRooms");
    }
  },
  components: {
    RoomCard
  },

  mounted() {
    this.$store.dispatch("loadRooms");
  }

}

</script>

<style scoped>
#fondo div:hover {
  background-color: rgba(61, 126, 166, 0.5);
  border-radius: 15px;
}

li {
  list-style: none;
  margin-bottom: 10px;
}
</style>
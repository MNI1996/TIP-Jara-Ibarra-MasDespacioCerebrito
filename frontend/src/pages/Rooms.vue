<template>
  <div v-if="searchedRoom!==null">
    <div style="margin-bottom: 20px ;align-content: center">
      <input v-model="id" type="text">
      <button @click="searchRoom" class="btn btn-lg btn-success">Buscar sala</button>
    </div>
    <room-card :room="searchedRoom"/>
    <button @click="goBacK" class="btn btn-lg btn-success">Volver a Salas</button>
    <button @click="loadRooms" class="btn btn-lg btn-success">Recargar Salas</button>
  </div>

  <div v-else>
    <template v-if="rooms.length > 0">
      <div style="margin-bottom: 20px ;align-content: center">
        <input v-model="id" type="text">
        <button @click="searchRoom" class="btn btn-lg btn-success">Buscar sala</button>
        <button @click="goToCreateARoom" class="btn btn-lg btn-success">Crear sala</button>
      </div>
      <div id="rooms-table">
        <div class="row justify-content-center">
          <div class="titles col col-md-3"><h3><strong>Nombre</strong></h3></div>
          <div class="titles col col-md-3"><h3><strong>Creador</strong></h3></div>
          <div class="titles col col-md-3"><h3><strong>Jugadores</strong></h3></div>
          <div class="titles col col-md-2"></div>
        </div>
        <div v-for="room in rooms">
          <room-card :room="room"/>
        </div>
      </div>
      <button @click="loadRooms" class="btn btn-lg btn-success btn-block">Recargar Salas</button>
    </template>
    <template v-else>
      <h1>No hay salas en este momento</h1>
      <div class="row">
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
    goBacK() {
      this.$store.dispatch("resetSearch")
      this.id = null
    },
    goToCreateARoom() {
      this.$store.commit('setCurrentRoomId', this.nextRoomId);
      this.$router.push({name: "create_room"})
    },
    searchRoom() {
      this.$store.dispatch("getSearchedRoom", this.id)
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
    this.$noty.success("Bienvenido a Mas Despacio Cerebrito")

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
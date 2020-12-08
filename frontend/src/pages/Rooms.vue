<template>
  <div class="col-12 col-md-7">
    <div class="darkslate-panel mdc-border slide-in-right" v-if="searchedRooms.length > 0  || rooms.length > 0">
      <div class="row search-and-create">
        <div class="col-12 col-md-7">
          <input class="mdc-rounded" @keyup.enter="searchRoom" v-model="id" type="text"
                 placeholder="Ingresa nombre de sala o creador" maxlength="18">
          <img @click="searchRoom" src="Images/magnifying-glass.png" class="search-img">
          <img v-if="id" @click="goBacK" src="Images/delete.png" class="delete-img">
        </div>
        <div class="col-6 col-md-5">
          <button @click="goToCreateARoom" class="btn btn-lg btn-success btn-block">Crear sala</button>
        </div>
      </div>
      <div id="rooms-table">
        <div class="row">
          <div class="col-11 room-card mdc-border">
            <div class="row">
              <div class="col-5 col-md-5"><h3 class="room-card-titles name">Nombre de sala</h3></div>
              <div class="col-3 col-md-3"><h3 class="room-card-titles">Creador</h3></div>
              <div class="col-2 col-md-2"><h3 class="room-card-titles">Jugadores</h3></div>
              <div class="col-1 col-md-1"></div>
            </div>
          </div>
        </div>
        <room-card v-if="searchedRooms.length > 0" v-for="room in searchedRooms" :room="room" :key="room._id"/>
        <room-card v-if="!searchedRooms.length > 0" v-for="room in rooms" :room="room" :key="room._id"/>
      </div>
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
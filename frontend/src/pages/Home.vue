<template>
  <div class="row home-container">
    <div class="col-10 col-md-5">
      <img src="Images/Logo.png" alt="Brainy" class="img-fluid logo-home">
    </div>
    <authentication v-if="!player"/>
    <rooms id="rooms" v-if="logged"/>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import Rooms from "./Rooms.vue";
import Authentication from "../components/Authentication.vue";

export default {
  name: "Home",
  components: {Authentication, Rooms},
  computed: {
    ...mapGetters(["player", "logged"]),
  },
  mounted(){
    this.refreshRoomsEachMinute()
  },
  beforeRouteEnter (to, from, next) {
    next(vm => {
      vm.$store.dispatch('resetDataRelatedToAGame');
    })
  },
  beforeRouteUpdate (to, from, next) {
    this.$store.dispatch('resetDataRelatedToAGame');
  },
  methods:{
    refreshRoomsEachMinute(){
      this.$store.dispatch('loadRooms');
      setTimeout(this.refreshRoomsEachMinute,60000);
    }
  }
}
</script>

<template>
  <div class="text-center row" id="margen">
    <div class="col-10 col-sm-6">
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
}
</script>

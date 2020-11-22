<template>
  <div class="text-center, row" id="margen">
      <authentication v-if="!player"/>
      <rooms v-if="logged"/>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import Rooms from "./Rooms.vue";
import Authentication from "../components/Authentication.vue";

export default {
  name: "Home",
  components: {Authentication, Rooms},
  computed:{
    ...mapGetters(["player","logged"]),
  },
}
</script>

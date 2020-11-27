<template>
  <div>
    <template v-if="player">
      <div id="mods" style="background-image: url('Images/background tapestry.png');" class="row">
        <div class="col" style="align-items: center;display: flex">
          <p>
            {{ playerNick.toString().toUpperCase() }}
          </p>
        </div>
        <div class="col" style="display: flex;align-items: center">
          <h1 style="color: aliceblue"> Total Points: {{ playerPoints }}</h1>
        </div>
      </div>
    </template>
    <template v-else>
      <user-login/>
    </template>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import UserLogin from "../components/UserLogin.vue";

export default {
  name: "Profile",
  components: {UserLogin},
  computed: {
    ...mapGetters(["player"]),
    playerNick() {
      if (this.player !== null) {
        return this.player['_id'];
      }
    },
    playerPoints() {
      if (this.player !== null) {
        return this.player.points;
      } else {
        return 0;
      }
    },
  },
  beforeRouteEnter(to, from, next) {
    next(vm => {
      // access to component instance via `vm`
      if (!vm.$store.getters.logged) next({name: 'home'})
      vm.$store.dispatch('loadPlayer');
    })
  },
  beforeRouteUpdate(to, from, next) {
    if (!this.$store.getters.logged) next({name: 'home'})
    this.$store.dispatch('loadPlayer');
    next()
  },
}
</script>
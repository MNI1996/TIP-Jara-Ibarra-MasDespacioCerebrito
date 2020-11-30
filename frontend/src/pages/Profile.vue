<template>
  <div class="row col-12 col-md-10 offset-md-1 game-information">
    <div class="col-12 col-md-7">
      <div class="row">
        <div class="col-12 col-md-3 game-info-div">
          <div class="row">
            <h2>{{ playerNick }}</h2>
          </div>
        </div>
        <div class="col-12 col-md-8 offset-md-1 game-info-div">
          <div class="row">
            <h2>Puntos totales: {{playerPoints}}</h2>
          </div>
        </div>
      </div>
    </div>
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
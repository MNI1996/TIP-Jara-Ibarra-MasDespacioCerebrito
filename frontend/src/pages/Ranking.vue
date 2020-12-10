<template>
  <div id="ranking" class="col-12 col-md-6 offset-md-3 mdc-border">
    <div class="col-12 additional">
        <h1 class="players-ranking-title">Ranking de jugadores</h1>
    </div>
    <div class="col-10 offset-1 game-info-div mdc-border">
        <div class="row justify-content-center">
        <div class="titles col-5">
          <h3>
            <strong>Jugador</strong>
          </h3>
        </div>
        <div class="titles col-5">
          <h3>
            <strong>Puntos</strong>
          </h3>
        </div>
      </div>

    </div>
    <div class="col-10 offset-1">
      <div v-for="player in playersRanking" class="row justify-content-center ranking-rows">
        <div class="ranking-player col-5">
          <h3>
            {{ player._id }}
          </h3>
        </div>
        <div class="ranking-points col-5">
          <h3>
            {{ player.points }}
          </h3>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "Ranking",
  computed: {
    ...mapGetters(["playersRanking"]),
  },
  beforeRouteEnter(to, from, next) {
    next(vm => {
      // access to component instance via `vm`
      if(!vm.$store.getters.logged) next({name:'home'})
      vm.$store.dispatch('loadPlayersRanking');
    })
  },
  beforeRouteUpdate(to, from, next) {
    if(!this.$store.getters.logged) next({name:'home'})
    this.$store.dispatch('loadPlayersRanking');
    next()
  },
}
</script>
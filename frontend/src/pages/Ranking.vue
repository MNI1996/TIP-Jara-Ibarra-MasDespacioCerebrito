<template>
  <div id="ranking" class="col-12">
    <div class="col-12 col-md-8 offset-md-2 additional">
        <h1 class="players-ranking-title">Ranking de jugadores</h1>
    </div>
    <div class="row justify-content-center">
          <div class="titles col col-md-4">
            <h3>
              <strong>Jugador</strong>
            </h3>
          </div>
          <div class="titles col col-md-4">
            <h3>
            <strong>Puntos</strong>
          </h3>
          </div>
    </div>
    <div v-for="player in playersRanking" class="row justify-content-center">
          <div class="ranking-player col col-md-4">
            <h3>
              {{ player._id }}
            </h3>
          </div>
          <div class="ranking-points col col-md-4">
            <h3>
              {{ player.points }}
            </h3>
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
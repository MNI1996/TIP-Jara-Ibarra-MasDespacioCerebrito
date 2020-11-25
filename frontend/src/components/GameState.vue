<template>
  <div class="fixed-bottom game-state-container">
    <div class="col-md-4 offset-md-4 row game-state-row" v-for="(state,index) in gameState">
        <div class="col-md-2 text-center">
          <img v-if="index === 0 && state.points > 0" class="img-fluid" src="Images/trophy.png">
          <img v-if="index === 1 && state.points > 0" class="img-fluid" src="Images/silver-medal.png">
          <img v-if="index === 2 && state.points > 0" class="img-fluid" src="Images/bronze-medal.png">
        </div>
        <div class="col-md-6 text-center"> {{state.player}}</div>
        <div class="col-md-4 text-center"> {{state.points}}</div>
    </div>
  </div>
</template>

<script>
export default {
  name: "GameState",
  props: {
    gameState: {type: Array}
  },
}
</script>

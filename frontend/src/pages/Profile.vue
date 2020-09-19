<template>
  <h1>Nick: {{playerNick}} | Total Points: {{playerPoints}}</h1>
</template>

<script>
import {mapGetters} from "vuex";

export default {
name: "Profile",
  computed: {
    ...mapGetters(["player"]),
    playerNick(){
      if(this.player !== null){
        return this.player['_id'];
      }
    },
    playerPoints(){
      if(this.player !== null){
        return this.player.points;
      }else{
        return 0;
      }
    },
  },



  mounted(){
    this.changeBackground();
  },


  methods:{
      changeBackground()
      {
        var index=document.getElementById('body')
        index.style.cssText="background-color:#0000FF;"
      }
    },

  beforeRouteEnter (to, from, next) {
    // called before the route that renders this component is confirmed.
    // does NOT have access to `this` component instance,
    // because it has not been created yet when this guard is called!
      next(vm => {
        // access to component instance via `vm`
        vm.$store.dispatch('loadPlayer');
      })
  },
  beforeRouteUpdate (to, from, next) {
    // called when the route that renders this component has changed.
    // This component being reused (by using an explicit `key`) in the new route or not doesn't change anything.
    // For example, for a route with dynamic params `/foo/:id`, when we
    // navigate between `/foo/1` and `/foo/2`, the same `Foo` component instance
    // will be reused (unless you provided a `key` to `<router-view>`), and this hook will be called when that happens.
    // has access to `this` component instance.
    this.$store.dispatch('loadPlayer');
  },
}
</script>

<style scoped>

</style>
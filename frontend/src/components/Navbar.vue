<template>
  <div class="row">
    <div class="navbar navbar-mdc col-12">
      <div class="row d-sm-none col-10 offset-1" v-if="logged">
        <div class="col col-4">
          <router-link :to="{name: 'home'}">
            <img src="Images/house.png" class="img-fluid heartbeat">
          </router-link>
        </div>
        <div class="col col-4">
          <router-link :to="{name: 'ranking'}">
            <img src="Images/podium.png" class="img-fluid heartbeat">
          </router-link>
        </div>

        <div class="col col-4">
          <router-link :to="{name: 'profile'}">
            <img :src="`Images/avatars/${avatarImage}.png`" class="img-fluid heartbeat">
          </router-link>
        </div>
      </div>

      <div class="col-12 d-sm-none">
        <img src="Images/logonombre.png" alt="Brainy" class="img-fluid">
      </div>

      <div :class="{'col-12': !logged}" class="col-7 d-none d-sm-block">
        <img src="Images/logonombre.png" alt="Brainy" class="img-fluid">
      </div>

      <div class="col-5 d-none d-sm-block" v-if="logged">
        <div class="col-12 row">
          <div class="col-3">
            <router-link :to="{name: 'home'}">
              <img src="Images/house.png" class="img-fluid heartbeat">
            </router-link>
          </div>
          <div class="col-3">
            <router-link :to="{name: 'ranking'}">
              <img src="Images/podium.png" class="img-fluid heartbeat">
            </router-link>
          </div>

          <div class="col-3">
            <router-link :to="{name: 'profile'}">
              <img :src="`Images/avatars/${avatarImage}.png`" class="img-fluid heartbeat">
            </router-link>
          </div>

        </div>
      </div>

    </div>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "Navbar",
    computed: {
    ...mapGetters(["logged", "player"]),
      avatarImage(){
        return this.player && this.player.avatar_image_name ? this.player.avatar_image_name : 'man';
      }
  }
}
</script>

<style scoped>

</style>
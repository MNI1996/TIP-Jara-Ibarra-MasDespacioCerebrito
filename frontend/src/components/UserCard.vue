<template>
  <div class="user-card">
    <img :src="`Images/avatars/${avatarImage}.png`" class="img-fluid user-card-img">
    <p class="user-card-p">{{dato}}</p>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
name: "UserCard",
  props: {dato:String},
  computed: {
      ...mapGetters(["players"]),
      avatarImage(){
        let player = this.players.find(p => p._id===this.dato);
        return player && player.avatar_image_name ? player.avatar_image_name : 'man';
      }
  }
}
</script>
<template>
  <div class="row col-12 col-md-10 offset-md-1 game-information mdc-border margin-bottom-end">
    <div class="col-12 col-md-7">
      <div class="row">
        <div class="col-12 col-md-3">
          <div class="row game-info-div">
            <img :src="`Images/avatars/${currentPlayerAvatarImage}.png`" class="img-fluid heartbeat">
          </div>
          <div class="row game-info-div">
            <h2>{{ playerNick }}</h2>
          </div>
        </div>
        <div class="col-12 col-md-8 offset-md-1">
          <div class="row game-info-div">
            <div class="col-12">
              <h2>Puntos totales: {{ playerPoints }}</h2>
            </div>
            <div class="col-12">
              <button @click="doShowModal" class="btn btn-lg btn-info btn-logout">Cambiar Imagen</button>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          <div class="row">
            <button @click="logout" class="btn btn-lg btn-danger btn-logout">Cerrar Sesión</button>
          </div>
        </div>
      </div>
    </div>
    <images-modal v-if="showModal" @hideModal="hideModal"/>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import UserLogin from "../components/UserLogin.vue";
import ImagesModal from "../components/ImagesModal.vue";

export default {
  name: "Profile",
  components: {ImagesModal, UserLogin},
  data() {
    return {
      showModal: false
    }
  },
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
    currentPlayerAvatarImage() {
      return this.player && this.player.avatar_image_name ? this.player.avatar_image_name : 'man' ;
    }
  },
  methods: {
    logout() {
      this.$store.dispatch("logout");
      this.$router.push({name: 'home'})
    },
    doShowModal(){
      this.showModal = true;
    },
    hideModal(){
      this.showModal = false;
    }
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
<template>
  <div class="row col-12 col-md-10 game-information mdc-border images-modal margin-bottom-end">
    <div class="row">
      <div class="col-12">
        <div class="row flex-container">
          <div class="center-card" v-for="avatarImage in avatarImages" :key="avatarImage"
               @click="selectImage(avatarImage)">
            <div class="catCard" :class="{selected: isImageSelected(avatarImage)}">
              <img :src="`Images/avatars/${avatarImage}.png`" class="img-fluid heartbeat-category"
                   @click="selectImage(avatarImage)">
            </div>

          </div>
        </div>
      </div>
      <div class="col-12">
        <button @click="changeImage" class="btn btn-lg btn-info btn-logout">Confirmar Imagen</button>
        <button @click="$emit('hideModal')" class="btn btn-lg btn-danger btn-logout">Cancelar</button>
      </div>
    </div>
  </div>

</template>

<script>
import {mapGetters} from "vuex";

export default {
  name: "ImagesModal",
  data() {
    return {
      imageSelected: null,
    }
  },
  mounted(){
    this.imageSelected = this.currentPlayerAvatarImage;
  },
  computed: {
    ...mapGetters(["player"]),
    avatarImages() {
      return ['man', 'woman', 'chef', 'pirate', 'firefighter', 'man_2', 'nun', 'woman_2', 'old_man', 'woman_3',
        'man_cca', 'woman_cca', 'man_3', 'cowboy', 'man_4', 'man_5', 'man_6', 'woman_4', 'doctor', 'old_woman'];
    },
    currentPlayerAvatarImage() {
      return this.player.avatar_image_name;
    }
  },
  methods: {
    changeImage() {
      this.$store.dispatch('updateImage', this.imageSelected);
      this.$emit('hideModal');
    },
    selectImage(avatarImage) {
      this.imageSelected = avatarImage;
    },
    isImageSelected(avatarImage) {
      return avatarImage === this.imageSelected;
    }
  },
}
</script>

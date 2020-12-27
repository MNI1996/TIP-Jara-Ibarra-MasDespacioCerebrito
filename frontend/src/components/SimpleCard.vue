<template>
  <div @click="$emit('addCategory', dato)" class="center-card">
      <p class="category-p" :class="{'no-margin-bottom': dato === 'Películas y Series'}">{{ dato }}</p>
    <div class="catCard" :class="{selected: isCatSelected()}">
      <img :src=generateUrl(dato) alt="" class="img-fluid heartbeat-category">
    </div>
  </div>

</template>

<script>
export default {
  name: "SimpleCard",
  props: {
    dato: String
  },
  methods: {
    generateUrl(name) {
      return "Images/Categories/" + name + ".png"
    },
    isCatSelected() {
      return this.$parent.roomCategories.includes(this.dato);
    }
  }
}
</script>

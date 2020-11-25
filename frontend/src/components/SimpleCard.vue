<template>
  <div @click="$emit('addCategory', dato)" class="catCard col-4 col-md-3" :class="{selected: isCatSelected()}">
    <p>{{ dato }}</p>
    <img :src=generateUrl(dato) alt="" class="img-fluid category-image">
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

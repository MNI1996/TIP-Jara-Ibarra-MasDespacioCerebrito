<template>
  <div @click="$emit('addCategory', dato)" class="col-4 col-md-3 center-card">
      <p>{{ dato }}</p>
    <div class="col-md-8 catCard" :class="{selected: isCatSelected()}">
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

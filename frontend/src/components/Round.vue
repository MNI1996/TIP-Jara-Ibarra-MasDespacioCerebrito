<template>
  <question :question="question"/>
</template>

<script>
import Question from "./Question.vue";

export default {
  name: "Round",
  props:{
    question :Object,

  },
  components:{Question}
}
</script>

<style scoped>

</style>
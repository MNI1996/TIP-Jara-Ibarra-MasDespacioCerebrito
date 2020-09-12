<template>
 <div class="text-center">
   <h1>Welcome to the test Room</h1>
   <h2>Points {{points}}</h2>
   <template v-if="hasQuestions">
      <h1 v-if="isOver">Game finished</h1>
      <question v-else :question="questions[currentQuestion]"/>
   </template>
 </div>
</template>

<script>
import {mapGetters} from "vuex";
import Question from "../components/Question.vue";

export default {
  name: "Room",
  components: {Question},
  computed:{
    ...mapGetters(["questions", "points", "currentQuestion"]),
    isOver(){
      return this.currentQuestion >= this.questions.length
    },
    hasQuestions(){
      return this.questions.length > 0;
    }
  },
  created() {
    this.$store.dispatch('loadQuestions');
  }
}
</script>

<style scoped>

</style>
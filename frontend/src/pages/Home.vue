<template>
  <div>
      <h1>This is the Home</h1>
      <button @click="loadQuestions">Load Questions</button>
      <h1>Questions</h1>
      <ul>
        <li v-for="question in questions">{{question.text}}</li>
      </ul>
  </div>
</template>

<script>
export default {
  name: "Home",
  computed:{
    questions(){
      return this.$store.getters.questions;
    }
  },
  methods:{
    loadQuestions(){
        this.$store.dispatch("loadQuestions");
    }
  }
}
</script>

<style scoped>

</style>
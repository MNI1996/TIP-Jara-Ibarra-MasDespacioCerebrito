<template>
  <div>
      <h1>This is the Home</h1>
      <button @click="loadQuestions">Load Questions</button>
      <h1>Questions</h1>
      <ul>
        <li v-for="question in questions">
          <h2>{{question.text}}</h2>
          <div>
              <button v-for="option in question.options" class="btn-block">{{ option.sentence }}</button>
          </div>
        </li>
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
.boton div
{
  display: block;
}
.boton div:hover
{
  background-color:#666
}
.options div
{
  background-color: aqua;
}
.btn-block:hover{
  background-color: coral;
}
</style>
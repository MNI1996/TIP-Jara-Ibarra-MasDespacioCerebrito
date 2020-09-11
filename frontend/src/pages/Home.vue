<template>
  <div>
      <h1>This is the Home</h1>
      <button @click="loadQuestions">Load Questions</button>
      <h1>Questions</h1>
      <ul>
        <li v-for="question in questions">
          <h2>
            {{question.text}}
          </h2>
          <div class="row ,options">
            <div class ="col-md-4 , boton"  @click="question.options[0][2]">
              <h3>{{question.options[0]["sentence"]}}</h3>
            </div>
            <div class ="col-md-4 boton"   @click="question.options[1]">
              <h3>{{question.options[1]["sentence"]}}</h3>
            </div>
            <div class ="col-md-4 boton"   @click="question.options[2]">
              <h3>{{question.options[2]["sentence"]}}</h3>
            </div>
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
</style>
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
          <div class="row" v-for="option in questions.options">
            <div class ="col-md-4" id="boton">
              <h3>option.sentence</h3>
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
#boton hover
{
  background-color:#fff
}

</style>
<template>
    <div>
        <h2>{{question.text}}</h2>
        <div class="row">
          <div class="col"  v-for="option in question.options">
            <button class="btn-block" style="font-size: 15px;" @click="answerQuestion(option)">{{ option.sentence }}</button>
          </div>
        </div>
    </div>
</template>

<script>
export default {
  name: "Question",
  props:{
    question: Object,
  },
  data(){
    return {
      answered: false,
    }
  },
  methods:{
    answerQuestion(option){
      this.$store.dispatch('answerQuestion',{questionId: this.question._id.$oid,option})
    }
  }
}
</script>

<style scoped>
.btn-block:hover{
  background-color: coral;
}
</style>
<template>
    <div>
        <h2>{{question.text}}</h2>
        <div>
            <button v-for="option in question.options" class="btn-block" @click="answerQuestion(option)">{{ option.sentence }}</button>
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

</style>
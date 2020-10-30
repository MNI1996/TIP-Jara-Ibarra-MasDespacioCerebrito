<template>
    <div>
        <h2 style="color: aliceblue">{{question.text}}</h2>
        <div class="row">
          <div class="col" id="area" v-for="option in question.options">
            <a  style="font-size: 20px; color: aliceblue;" @click="answerQuestion(option)"   >
              <div style="height: 90px;  width: 120px; align-items: center;display: flex; justify-content: center;">
                <p>{{ option.sentence }}</p>
              </div>
            </a>
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
#area div:hover{
  background-color: rgba(0, 0, 0,0.25);
  border-radius: 15px;

}
</style>
<template>
    <div>
        <h2 style="color: aliceblue">{{question.text}}</h2>
        <div class="row">
          <div class="col" id="area" v-for="option in question.options">
            <a  style="font-size: 20px; color: aliceblue;" @click="answerQuestion(option)"   >
              <div :class="{correct: option.correct, incorrect: !option.correct}" style="height: 90px;  width: 120px; align-items: center;display: flex; justify-content: center;">
                <p>{{ option.sentence }}</p>
              </div>
            </a>
          </div>
        </div>
    </div>
</template>

<script>
import {mapGetters} from "vuex";

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
  computed: {
     ...mapGetters(["currentRoom"]),
  },
  methods:{
    async answerQuestion(option){
      await this.$store.dispatch('answerQuestion',{questionId: this.question._id.$oid,option})
      this.$parent.$parent.socket.emit('player_answered', {room:this.currentRoom._id, question_id: this.question._id.$oid});
    }
  }
}
</script>

<style scoped>
#area div:hover{
  background-color: rgba(0, 0, 0,0.25);
  border-radius: 15px;

}
.show_answer .incorrect{
    background-color: red;
}
.show_answer .correct{
    background-color: green;
}
</style>
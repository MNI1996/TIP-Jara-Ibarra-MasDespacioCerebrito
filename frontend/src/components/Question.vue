<template>
    <div>
        <h2 class="letra">{{question.text}}</h2>
        <div class="col justify-content-center">
          <div :class="{correct: option.correct, incorrect: !option.correct, active: isSelected(option)}"
               class="col-12 option"
               v-for="option in question.options"
               @click="selectOption(option)">
                <p>{{ option.sentence }}</p>
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
      selected: null,
    }
  },
  computed: {
     ...mapGetters(["currentRoom"]),
  },
  methods:{
    async answerQuestion(option){
      await this.$store.dispatch('answerQuestion',{questionId: this.question._id.$oid,option})
      this.$parent.$parent.socket.emit('player_answered', {room:this.currentRoom._id, question_id: this.question._id.$oid});
    },
    isSelected(option){
       return this.selected !== null && this.selected === option;
    },
    selectOption(option){
      this.selected = option;
    }
  }
}
</script>
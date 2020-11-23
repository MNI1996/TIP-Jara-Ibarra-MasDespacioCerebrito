<template>
    <div>
        <h2 class="letra">Tiempo: {{countdown}}</h2>
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
      roundTime: 10,
      currentTime: 0,
    }
  },
  computed: {
     ...mapGetters(["currentRoom"]),
    countdown(){
       return this.roundTime - this.currentTime;
    }
  },
  methods:{
    async answerQuestion(){
      let selectedOption = this.selected;
      await this.$store.dispatch('answerQuestion',{questionId: this.question._id.$oid, option: selectedOption})
      this.$parent.$parent.socket.emit('player_answered', {room:this.currentRoom._id, question_id: this.question._id.$oid});
    },
    isSelected(option){
       return this.selected !== null && this.selected === option;
    },
    selectOption(option){
      this.selected = option;
    },
    startRound(){
      setTimeout(() => {
        if(this.currentTime >= this.roundTime){
          this.answerQuestion();
          this.$parent.$parent.endRoundForOwner()
          this.currentTime = 0;
          this.selected = null;
          return ;
        }
        this.addOne();
        this.startRound();
    }, 1000);

    },
    addOne(){
      this.currentTime = this.currentTime + 1;
    }
  }
}
</script>
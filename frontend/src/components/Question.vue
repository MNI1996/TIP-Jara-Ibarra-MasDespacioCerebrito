<template>
    <div class="game-creation col-12 slide-out-left slide-in-right">
        <h2 class="question-text">{{question.text}}</h2>
        <div class="col justify-content-center">
          <button :class="{correct: option.correct, incorrect: !option.correct, active: isSelected(option)}"
                  class="btn btn-lg col-12 option"
                  v-for="option in options"
                  @click="selectOption(option)"
                  :disabled="answered"
                  :id="'button-'+option._id.$oid">
            {{ option.sentence }}
          </button>
        </div>
        <button class="btn btn-lg btn-success" @click="answerQuestion()" :disabled="!selected || answered" id="btn-enviar-respuesta">Enviar Respuesta</button>
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
    roundTime(){
       return this.currentRoom.round_time
    },
    options(){
       return this.shuffle(this.question.options);
    }
  },
  methods:{
    async answerQuestion(){
      let selectedOption = this.selected;
      await this.$store.dispatch('answerQuestion',{questionId: this.question._id.$oid, option: selectedOption})
      this.$parent.$parent.socket.emit('player_answered', {room:this.currentRoom._id, question_id: this.question._id.$oid});
      this.answered = true;
    },
    isSelected(option){
       return this.selected !== null && this.selected === option;
    },
    selectOption(option){
      this.selected = option;
    },
    startRound(){
      setTimeout(() => {
        if(this.$parent.$parent.currentTime >= this.roundTime){
          if (!this.answered){
            this.answerQuestion();
          }
          this.$parent.$parent.endRoundForOwner()
          return ;
        }
        this.$parent.$parent.addOne();
        this.startRound();
    }, 1000);

    },
    resetComponent(){
      this.$parent.$parent.currentTime = 0;
      this.selected = null;
      this.answered = false;
    },
    shuffle(array) {
      var currentIndex = array.length, temporaryValue, randomIndex;

      // While there remain elements to shuffle...
      while (0 !== currentIndex) {

        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;

        // And swap it with the current element.
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
      }

      return array;
    }
  }
}
</script>
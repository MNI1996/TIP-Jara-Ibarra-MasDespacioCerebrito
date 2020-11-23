<template>
  <question ref="refQuestion" :question="this.getQ()[0]"/>
</template>

<script>
import Question from "./Question.vue";
import {mapGetters} from "vuex";

export default {
  name: "Round",
  props:{
    question :Object,


  },
  components:{Question},
  computed: {...mapGetters(["questions"])},
  methods:
      {
        searched(value){
          return value._id.$oid === this.question.$oid
        },
        getQ(){
          return this.questions.filter((e)=> this.searched(e))
        }
      }


}
</script>

<style scoped>

</style>
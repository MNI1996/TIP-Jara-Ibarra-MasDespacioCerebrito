import Vue from 'vue'
import Vuex from 'vuex'
import createLogger from "vuex/dist/logger";

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'
const apiUrl = "http://localhost:5000/questions/"

export default new Vuex.Store({
  strict: debug,
  plugins: debug ? [createLogger()] : [],
  state:{
    rooms: [],
    questions: [],
  },
  getters:{
    questions: (state) => state.questions,
  },
  mutations: {
    setQuestions: (state, questions) => state.questions = questions,
  },
  actions: {
    async loadQuestions({commit}){
      let response = await Vue.axios.get(apiUrl);
      commit('setQuestions', response.data.result)
    }
  },
})
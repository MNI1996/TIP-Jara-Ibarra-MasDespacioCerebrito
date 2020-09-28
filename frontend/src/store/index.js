import Vue from 'vue'
import Vuex from 'vuex'
import createLogger from "vuex/dist/logger";

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'
const apiUrl = "http://localhost:5000"

export default new Vuex.Store({
  strict: debug,
  plugins: debug ? [createLogger()] : [],
  state:{
    rooms: [],
    questions: [],
    points: 0,
    currentQuestion: 0,
    player: null,
    currentRoom: null,
  },
  getters:{
    questions: (state) => state.questions,
    currentQuestion: (state) => state.currentQuestion,
    currentRoom: (state) => state.currentRoom,
    points: (state) => state.points,
    player: (state) => state.player,
    rooms: (state) => state.rooms,
    nextRoomId: (state) => {
      if(state.currentRoom){
        return state.currentRoom;
      }
      return state.rooms.length + 1;
    },
  },
  mutations: {
    setQuestions: (state, questions) => state.questions = questions,
    setPlayer: (state, player) => state.player = player,
    setRooms: (state, rooms) => state.rooms = rooms,
    addPoint: (state, answer) => {
      if(answer){
        state.points++;
      }
    },
    nextQuestion: (state) => {
        state.currentQuestion++;
    },
    setCurrentRoom: (state, roomId) => state.currentRoom = roomId,
  },
  actions: {
    async loadQuestions({commit}){
      let response = await Vue.axios.get(apiUrl+"/questions/");
      commit('setQuestions', response.data.result)
    },
    async answerQuestion({commit, state}, {questionId, option}){
      let data = {
        id: option._id.$oid,
        sentence: option.sentence,
        nick: state.player._id,
      }
      let response = await Vue.axios.post(apiUrl+"/question/"+questionId+"/",{data:data});
      commit('addPoint', response.data.result)
      commit('nextQuestion')
    },
    async loadPlayer({commit,state}){
      if(state.player && state.player._id){
        let response = await Vue.axios.get(`${apiUrl}/players/?nick=${state.player._id}`);
        commit('setPlayer', response.data.result)
      }
    },
    async loadRooms({commit}){
      let response = await Vue.axios.get(apiUrl+"/rooms/");
      commit('setRooms', response.data.result)
    },
    async login({commit}, nick){
      let response = await Vue.axios.post(apiUrl+"/players/", {nick:nick});
      commit('setPlayer', response.data.result)
    }
  },
})
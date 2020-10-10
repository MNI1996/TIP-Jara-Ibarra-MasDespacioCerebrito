import Vue from 'vue'
import Vuex from 'vuex'
import createLogger from "vuex/dist/logger";

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'
const apiUrl = "http://localhost:5000"
const categories={
    0:"Artes",
    1:"Fisica",
    2:"Quimica",
    3:"Biologia",
    4:"Historia",
    5:"Geografia",
    6:"Literatura",
    7:"Matematicas",
}
export default new Vuex.Store({
  strict: debug,
  plugins: debug ? [createLogger()] : [],
  state:{
    rooms: [],
    questions: [],
    points: 0,
    currentQuestion: 0,
    player: null,
    currentRoomId: null,
    logged: false,
    categories:categories,
    roomCategories:[]
  },
  getters:{
    questions: (state) => state.questions,
    currentQuestion: (state) => state.currentQuestion,
    currentRoomId: (state) => state.currentRoomId,
    points: (state) => state.points,
    player: (state) => state.player,
    rooms: (state) => state.rooms,
    logged:(state)=> state.logged,
    categories:(state)=>state.categories,
    roomCategories:(state)=>state.roomCategories,
    nextRoomId: (state) => {
      if(state.currentRoomId){
        return state.currentRoomId;
      }
      return state.rooms.length + 1;
    },
    isOwner: (state) => {
      return state.player && state.rooms && state.currentRoomId && state.player._id === state.rooms.find(room => room._id === state.currentRoomId).owner;
    },
    currentRoom: (state) => {
      if(state.currentRoomId && state.rooms && state.rooms.length > 0){
        return state.rooms.find(room => room._id === state.currentRoomId)
      }else{
        return null;
      }
    },
  },
  mutations: {
    setQuestions: (state, questions) => state.questions = questions,
    setPlayer: (state, player) => state.player = player,
    setRooms: (state, rooms) => state.rooms = rooms,
    setLogged: (state,logged) => state.logged=logged,
    addPoint: (state, answer) => {
      if(answer){
        state.points++;
      }
    },
    nextQuestion: (state) => {
        state.currentQuestion++;
    },
    addCategorie: (state,categorie)=>{
      let cond=state.roomCategories.includes(categorie["categorie"])
      if (!cond) {
       state.roomCategories= state.roomCategories.concat([categorie["categorie"]])
      }
    },
    setCurrentRoomId: (state, roomId) => state.currentRoomId = roomId,
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
      commit("setLogged",true)
    },
    async loadCategorie({commit,state}, categorie){
      commit("addCategorie",categorie)
    }
  },
})
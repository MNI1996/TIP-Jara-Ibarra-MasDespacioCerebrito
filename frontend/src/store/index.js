import Vue from 'vue'
import Vuex from 'vuex'
import createLogger from "vuex/dist/logger";

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'
const apiUrl = "http://localhost:5000"
const categories=["Artes", "Fisica", "Quimica", "Biologia", "Historia", "Geografia", "Literatura","Matematicas"];

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
    currentRoom: null,
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
    nextRoomId: (state) => {
      if(state.currentRoomId){
        return state.currentRoomId;
      }
      return state.rooms.length + 1;
    },
    isOwner: (state) => {
      return state.player && state.currentRoom && state.player._id === state.currentRoom.owner;
    },
    currentRoom: (state) =>  state.currentRoom,
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
    setCurrentRoomId: (state, roomId) => state.currentRoomId = roomId,
    setCurrentRoom: (state, room) => state.currentRoom = room,
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
    },
    async createRoom({commit, state, dispatch}, {name, categories}){
      let roomData = {'owner': state.player._id,
                     'name': name,
                     'categories': categories,
                     };
      let response = await Vue.axios.post(apiUrl+"/rooms/", roomData);
      commit("setCurrentRoom", response['data']['result']);
      dispatch("loadRooms");
    },
    async getRoom({commit}, roomId){
      let response = await Vue.axios.get(`${apiUrl}/rooms/${roomId}/`);
      commit("setCurrentRoom", response['data']['result']);
    }
  },
})
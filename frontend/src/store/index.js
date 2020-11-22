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
    searchedRoom:null,
    playersRanking: [],
    again:false
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
    searchedRoom:(state) =>state.searchedRoom,
    again:(state)=>state.again,
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
    playersRanking: (state) =>  state.playersRanking,
  },
  mutations: {
    setQuestions: (state, questions) => state.questions = questions,
    setPlayer: (state, player) => state.player = player,
    setRooms: (state, rooms) => state.rooms = rooms,
    setLogged: (state,logged) => state.logged=logged,
    setSearchedRoom:(state,searchedRoom) => state.searchedRoom=searchedRoom,
    resetSearchedRoom:(state)=>state.searchedRoom=null,
    resetCurrentRoom:(state)=>state.currentRoom=null,
    cleanCurrenQuestion:(state)=>state.currentQuestion=0,
    againSet:(state)=>state.again=true,
    resetAgain:(state)=>state.again=false,
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
    setPlayersRanking: (state, playersRanking) => state.playersRanking = playersRanking,
    setPoints: (state, points) => state.points = points,
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
        room_name: state.currentRoom._id
      }
      let response = await Vue.axios.post(apiUrl+"/question/"+questionId+"/",{data:data});
      commit('addPoint', response.data.result)
    },
    async loadPlayer({commit,state}){
      if(state.player && state.player._id){
        let response = await Vue.axios.get(`${apiUrl}/players/?nick=${state.player._id}`);
        commit('setPlayer', response.data.result)
      }
    },
      async getSearchedRoom({commit,state},id){
        let response=await Vue.axios.get(`${apiUrl}/rooms/${id}`)
        commit('setSearchedRoom',response.data.result)
      },
      async joinIt({commit,state},id){
        let response=await Vue.axios.get(`${apiUrl}/rooms/${id}`)
        if (state.searchedRoom != null){ commit("resetSearchedRoom")}
        commit('setCurrentRoom',response.data.result)
      },
      async resetSearch({commit}){
        commit('resetSearchedRoom')
      },

    async loadRooms({commit}){
      let response = await Vue.axios.get(apiUrl+"/rooms/");
      commit('setRooms', response.data.result)
    },
    async login({commit}, data){
      await Vue.axios.post(apiUrl+"/login/", data).then(response =>{
      commit('setPlayer', response.data.result)
      commit("setLogged",true)
      }).catch(() => Vue.noty.error("El nombre del jugador tiene que ser mayor a 3 carácteres"))
    },
    async register({commit}, data){
      await Vue.axios.post(apiUrl+"/register/", data).then(response =>{
      commit('setPlayer', response.data.result)
      commit("setLogged",true)
      }).catch(() => Vue.noty.error("El nombre del jugador tiene que ser mayor a 3 carácteres"))
    },
    async loadCategorie({commit,state}, categorie){
      commit("addCategorie",categorie)
    },
    async createRoom({commit, state, dispatch}, {name, categories,rounds}){
      let roomData = {'owner': state.player._id,
                      'name': name,
                      'categories': categories,
                      'rounds_amount':rounds,
                     };
      await Vue.axios.post(apiUrl+"/rooms/", roomData).then(response => {
        commit("setCurrentRoom", response['data']['result']);
        dispatch("loadRooms");
      }).catch(() =>{Vue.noty.error("El nombre de la sala tiene que tener al menos 5 carácteres")});
    },
    async cleanCurrentRoom({commit}){
      commit("resetCurrentRoom")
    },
    async resetQuestion({commit}){
      commit("cleanCurrenQuestion")
    },
    async loadPlayersRanking({commit}){
      await Vue.axios.get(apiUrl+"/ranking/players/").then(response => {
        console.log(response);
        commit("setPlayersRanking", response['data']['result'])
      }).catch(() =>{Vue.noty.error("Hubo un error obteniendo el ranking de jugadores")});
    },
    async updatePlayersInTheCurrentRoom({commit, state}){
      let currentRoomUpdated = state.rooms.filter(r => r._id === state.currentRoom._id);
      commit("setCurrentRoom", currentRoomUpdated[0]);
    },
    async resetPoints({commit}){
     commit("setPoints", 0);
    }
  },
})
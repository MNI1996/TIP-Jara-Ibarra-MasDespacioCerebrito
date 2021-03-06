import Vue from 'vue'
import Vuex from 'vuex'
import createLogger from "vuex/dist/logger";

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'
const apiUrl = "http://localhost:5000"
const categories = ["Películas y Series","Artes", "Música", "Deportes", "Física", "Química", "Biología", "Historia", "Geografía", "Literatura", "Matemáticas"];

function showErrorWithNoty(error) {
    if (error.response) {
        Vue.noty.error(error.response.data.message, {killer: true})
    } else if (error.message) {
        Vue.noty.error(error.message, {killer: true})
    } else {
        Vue.noty.error("Error desconocido", {killer: true})
    }
}

export default new Vuex.Store({
    strict: debug,
    plugins: debug ? [createLogger()] : [],
    state: {
        rooms: [],
        questions: [],
        points: 0,
        currentQuestion: 0,
        player: null,
        currentRoomId: null,
        logged: false,
        categories: categories,
        currentRoom: null,
        searchedRooms: [],
        playersRanking: [],
        again: false,
        players: [],
    },
    getters: {
        questions: (state) => state.questions,
        currentQuestion: (state) => state.currentQuestion,
        currentRoomId: (state) => state.currentRoomId,
        points: (state) => state.points,
        player: (state) => state.player,
        rooms: (state) => state.rooms,
        logged: (state) => state.logged,
        categories: (state) => state.categories,
        roomCategories: (state) => state.roomCategories,
        searchedRooms: (state) => state.searchedRooms,
        again: (state) => state.again,
        nextRoomId: (state) => {
            if (state.currentRoomId) {
                return state.currentRoomId;
            }
            return state.rooms.length + 1;
        },
        isOwner: (state) => {
            return state.player && state.currentRoom && state.player._id === state.currentRoom.owner;
        },
        currentRoom: (state) => state.currentRoom,
        playersRanking: (state) => state.playersRanking,
        players: (state) => state.players,
    },
    mutations: {
        setQuestions: (state, questions) => state.questions = questions,
        setPlayer: (state, player) => {
            state.player = player;
            if (player !== null) {
                Vue.$cookies.set('user', player);
            }
        },
        setRooms: (state, rooms) => state.rooms = rooms,
        setLogged: (state, logged) => state.logged = logged,
        setSearchedRooms: (state, searchedRooms) => state.searchedRooms = searchedRooms,
        resetSearchedRooms: (state) => state.searchedRooms = [],
        resetCurrentRoom: (state) => state.currentRoom = null,
        setCurrentQuestion: (state, currentQuestion) => state.currentQuestion = currentQuestion,
        cleanCurrenQuestion: (state) => state.currentQuestion = 0,
        againSet: (state) => state.again = true,
        resetAgain: (state) => state.again = false,
        setAgain: (state, again) => state.again = again,
        addPoint: (state, answer) => {
            if (answer) {
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
        setPlayers: (state, players) => state.players = players,
    },
    actions: {
        async loadQuestions({commit}) {
            await Vue.axios.get(apiUrl + "/questions/")
                .then(response => commit('setQuestions', response.data.result))
                .catch((error) => showErrorWithNoty(error));
        },
        async answerQuestion({commit, state}, {questionId, option}) {
            if (option !== null) {
                let data = {
                    id: option._id.$oid,
                    sentence: option.sentence,
                    nick: state.player._id,
                    room_name: state.currentRoom._id
                }
                await Vue.axios.post(apiUrl + "/question/" + questionId + "/", {data: data})
                    .then(response => commit('addPoint', response.data.result))
                    .catch((error) => showErrorWithNoty(error));
            }
        },
        async loadPlayer({commit, state}) {
            if (state.player && state.player._id) {
                await Vue.axios.get(`${apiUrl}/players/?nick=${state.player._id}`)
                    .then(response => commit('setPlayer', response.data.result))
                    .catch((error) => showErrorWithNoty(error));
            }
        },
        async getSearchedRooms({commit, state}, id) {
            await Vue.axios.get(`${apiUrl}/rooms/search/?q=${id}`)
                .then(response => commit('setSearchedRooms', response.data.result))
                .catch((error) => showErrorWithNoty(error));

        },
        async joinIt({commit, state}, id) {
            await Vue.axios.get(`${apiUrl}/rooms/${id}`)
                .then(response => {
                    if (state.searchedRooms.length > 0) {
                        commit("resetSearchedRooms")
                    }
                    commit('setCurrentRoom', response.data.result)
                })
                .catch((error) => {
                        if (error.response) {
                            if(error.response.status === 404){
                                Vue.noty.error("Esa sala ya no está disponible", {killer: true})
                            }else{
                                Vue.noty.error(error.response.data.message, {killer: true})
                            }
                        } else if (error.message) {
                            Vue.noty.error(error.message, {killer: true})
                        } else {
                            Vue.noty.error("Error desconocido", {killer: true})
                        }
                    }
                );
        },
        async resetSearch({commit}) {
            commit('resetSearchedRooms')
        },
        async loadRooms({commit}) {
            await Vue.axios.get(apiUrl + "/rooms/")
                .then(response => {
                    commit('setRooms', response.data.result)
                    commit('setPlayers', response.data.players)
                })
                .catch((error) => showErrorWithNoty(error));
        },
        async login({commit}, data) {
            await Vue.axios.post(apiUrl + "/login/", data).then(response => {
                commit('setPlayer', response.data.result)
                commit("setLogged", true)
                Vue.noty.success("Bienvenido a Mas Despacio Cerebrito", {killer: true})
            }).catch((error) => showErrorWithNoty(error));
        },
        async register({commit}, data) {
            await Vue.axios.post(apiUrl + "/register/", data)
                .then(response => {
                    commit('setPlayer', response.data.result)
                    commit("setLogged", true)
                    Vue.noty.success("Bienvenido a Mas Despacio Cerebrito", {killer: true})
                }).catch((error) => showErrorWithNoty(error));
        },
        async loadCategorie({commit, state}, categorie) {
            commit("addCategorie", categorie)
        },
        async createRoom({commit, state, dispatch}, {name, categories, rounds, round_time}) {
            let roomData = {
                'owner': state.player._id,
                'name': name,
                'categories': categories,
                'rounds_amount': rounds,
                'round_time': round_time,
            };
            await Vue.axios.post(apiUrl + "/rooms/", roomData)
                .then(response => {
                    commit("setCurrentRoom", response['data']['result']);
                    dispatch("loadRooms");
                }).catch((error) => {
                    if (error.response) {
                        Vue.noty.error("El nombre de la sala tiene que tener al menos 5 carácteres", {killer: true})
                    } else if (error.message) {
                        Vue.noty.error(error.message, {killer: true})
                    } else {
                        Vue.noty.error("Error desconocido", {killer: true})
                    }
                });
        },
        async cleanCurrentRoom({commit}) {
            commit("resetCurrentRoom")
        },
        async resetQuestion({commit}) {
            commit("cleanCurrenQuestion")
        },
        async loadPlayersRanking({commit}) {
            await Vue.axios.get(apiUrl + "/ranking/players/")
                .then(response => {
                    commit("setPlayersRanking", response['data']['result'])
                }).catch((error) => showErrorWithNoty(error));
        },
        async updatePlayersInTheCurrentRoom({commit, state}) {
            let currentRoomUpdated = state.rooms.filter(r => r._id === state.currentRoom._id);
            commit("setCurrentRoom", currentRoomUpdated[0]);
        },
        async resetPoints({commit}) {
            commit("setPoints", 0);
        },
        async resetDataRelatedToAGame({commit}) {
            commit("setCurrentRoom", null);
            commit("setCurrentQuestion", 0);
            commit("setPoints", 0);
            commit("setCurrentRoomId", null);
            commit("setSearchedRooms", []);
            commit("setAgain", false);
        },
        async refreshCurrentRoom({commit, state}) {
            await Vue.axios.get(`${apiUrl}/rooms/${state.currentRoom._id}/`)
                .then(response => {
                    commit('setCurrentRoom', response.data.result)
                    commit("setCurrentQuestion", 0);
                })
                .catch((error) => showErrorWithNoty(error));
        },
        async updateRoom({commit, state}, {categories, rounds, round_time}) {
            let roomData = {
                'categories': categories,
                'rounds_amount': rounds,
                'round_time': round_time,
            };
            await Vue.axios.post(`${apiUrl}/rooms/${state.currentRoom._id}/update/`, roomData)
                .then(response => {
                    commit("setCurrentRoom", response['data']['result']);
                    commit("setCurrentQuestion", 0);
                }).catch((error) => showErrorWithNoty(error));
        },
        async updateRoomWithSameState({commit, state}) {
            let roomData = {};
            await Vue.axios.post(`${apiUrl}/rooms/${state.currentRoom._id}/update/`, roomData)
                .then(response => {
                    commit("setCurrentRoom", response['data']['result']);
                    commit("setCurrentQuestion", 0);
                }).catch((error) => showErrorWithNoty(error));
        },
        logout({commit}) {
            Vue.$cookies.remove('user');
            commit('setPlayer', null);
            commit('setLogged', false);
        },
        async updateImage({commit, state}, imageSelected){
            let profileData = {
                'avatar_image': imageSelected,
            };
            await Vue.axios.post(`${apiUrl}/player/${state.player._id}/update/`, profileData)
                .then(response => {
                    commit("setPlayer", response['data']['result']);
                    Vue.noty.success("Imagen Actualizada Correctamente", {killer: true})
                }).catch((error) => showErrorWithNoty(error));

        }
    },
})
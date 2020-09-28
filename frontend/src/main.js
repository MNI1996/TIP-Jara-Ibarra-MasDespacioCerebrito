import Vue from 'vue'
import VueRouter from 'vue-router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import App from './App.vue'
import "../assets/app.css"
import 'es6-promise/auto'
import store from './store'
import Home from "./pages/Home.vue";
import Rooms from "./pages/Rooms.vue";
import Profile from "./pages/Profile.vue";
require('bootstrap');
import 'bootstrap/dist/css/bootstrap.min.css';
import Room from "./pages/Room.vue";
import CreateRoom from "./components/CreateRoom.vue";

Vue.use(VueAxios, axios)
Vue.use(VueRouter)
Vue.config.productionTip = false

const router = new VueRouter({
  routes: [
    { path: '/', name:"home", component: Home },
    { path: '/rooms', name: "rooms", component: Rooms },
    { path: '/profile', name: "profile", component: Profile },
    { path: '/room', name: "room", component: Room },
    { path: '/room/create', name: "create_room", component: CreateRoom },
  ]
})

new Vue({
  el: '#app',
  components: {App: App},
  store,
  router,
  render: h => h(App)
})
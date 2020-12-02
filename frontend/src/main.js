import Vue from 'vue'
import VueRouter from 'vue-router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import App from './App.vue'
import "../assets/app.css"
import 'vuejs-noty/dist/vuejs-noty.css'
import 'es6-promise/auto'
import VueNoty from 'vuejs-noty'
import store from './store'
import Home from "./pages/Home.vue";
import Rooms from "./pages/Rooms.vue";
import Profile from "./pages/Profile.vue";
require('bootstrap');
import 'bootstrap/dist/css/bootstrap.min.css';
import '../Styles.css';
import Room from "./pages/Room.vue";
import CreateRoom from "./components/CreateRoom.vue";
import Ranking from "./pages/Ranking.vue";
import VueCookies from 'vue-cookies'

Vue.use(VueCookies)
Vue.use(VueAxios, axios)
Vue.use(VueRouter)
Vue.use(VueNoty)
Vue.config.productionTip = false
Vue.$cookies.config('7d')

const router = new VueRouter({
  routes: [
    { path: '/', name:"home", component: Home },
    { path: '/rooms', name: "rooms", component: Rooms },
    { path: '/profile', name: "profile", component: Profile },
    { path: '/room', name: "room", component: Room },
    { path: '/room/create', name: "create_room", component: CreateRoom },
    { path: '/ranking/', name: "ranking", component: Ranking },
  ]
})

new Vue({
  el: '#app',
  components: {App: App},
  store,
  router,
  render: h => h(App)
})
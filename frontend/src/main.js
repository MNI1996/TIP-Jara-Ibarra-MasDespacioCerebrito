import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import "../assets/app.css"
import 'es6-promise/auto'
import store from './store'
import Home from "./pages/Home.vue";
import Rooms from "./pages/Rooms.vue";
import Profile from "./pages/Profile.vue";

Vue.use(VueRouter)
Vue.config.productionTip = false

const router = new VueRouter({
  routes: [
    { path: '/', name:"home", component: Home },
    { path: '/rooms', name: "rooms", component: Rooms },
    { path: '/profile', name: "profile", component: Profile },
  ]
})

new Vue({
  el: '#app',
  components: {App: App},
  store,
  router,
  render: h => h(App)
})
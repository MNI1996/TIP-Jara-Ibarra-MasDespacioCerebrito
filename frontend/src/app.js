import Vue from 'vue'
import App from './App.vue'
import "../assets/app.css"
import 'es6-promise/auto'
import store from './store'

new Vue({
  el: '#app',
  store,
  render: h => h(App)
})
<template>
  <div class="col-12 col-md-4 offset-md-1 authentication darkslate-panel">
    <register v-if="register" />
    <user-login v-else />
    <div class="register-or-login col-12 col-md-4 offset-md-4 col-lg-3 offset-lg-3">
        <button @click="toggleRegister" class="btn btn-lg btn-primary">{{registerOrLogin}}</button>
    </div>
  </div>
</template>

<script>
import UserLogin from "./UserLogin.vue";
import Register from "./Register.vue";

export default {
  name: "Authentication",
  components: {Register, UserLogin},
  data() {
    return {
      register: false,
    }
  },
  computed:{
    registerOrLogin(){
      return this.register ? "Ya tengo Usuario" : "No tengo usuario";
    }
  },
  methods:{
    toggleRegister(){
      this.register = !this.register;
    }
  }
}
</script>

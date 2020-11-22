<template>
  <div class="col authentication">
    <register v-if="register" />
    <user-login v-else />
    <div class="row register-or-login">
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

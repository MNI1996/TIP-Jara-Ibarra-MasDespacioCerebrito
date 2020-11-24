<template>
  <div class="col">
    <div class="row justify-content-start">
      <div class="col-6 col-md-4 col-lg-3 text-right">
        <label for="nick" class="letra">Usuario</label>
      </div>
      <div class="col-6 col-md-4 col-lg-3">
        <input v-model="nick" id="nick" type="text" maxlength="30">
      </div>
    </div>
    <div class="row justify-content-start">
      <div class="col-6 col-md-4 col-lg-3 text-right">
        <label for="pass" class="letra">Contraseña</label>
      </div>
      <div class="col-6 col-md-4 col-lg-3">
        <input v-model="password" id="pass" type="password" maxlength="30">
      </div>
    </div>
    <div class="boton-ingresar col-12 col-md-4 offset-md-4 col-lg-3 offset-lg-3">
      <button @click="login" class="btn btn-lg btn-success">Ingresar</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserLogin",
  data() {
    return {
      nick: "",
      password: "",
    }
  },
  methods: {
    login() {
      let data = {
        nick: this.nick,
        password: this.password,
      }
      this.$store.dispatch('login', data);
    }
  }
}
</script>
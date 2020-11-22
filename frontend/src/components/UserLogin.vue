<template>
  <div class="col">
    <div class="row justify-content-center">
      <div class="col-6 col-md-2 text-right">
        <label for="nick" class="letra">Usuario</label>
      </div>
      <div class="col-6 col-md-2">
        <input v-model="nick" id="nick" type="text" maxlength="30">
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="col-6 col-md-2 text-right">
        <label for="pass" class="letra">Contraseña</label>
      </div>
      <div class="col-6 col-md-2">
        <input v-model="password" id="pass" type="password" maxlength="30">
      </div>
    </div>
    <div class="row boton-ingresar">
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
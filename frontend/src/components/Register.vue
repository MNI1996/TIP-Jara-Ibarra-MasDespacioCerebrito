<template>
  <div class="col">
    <div class="row justify-content-center">
      <div class="col-6 col-md-4 col-lg-3 text-right">
        <label for="nick" class="letra">Elija su Usuario</label>
      </div>
      <div class="col-6 col-md-4 col-lg-3">
        <input v-model="nick" id="nick" type="text" maxlength="30">
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="col-6 col-md-4 col-lg-3 text-right">
        <label for="pass" class="letra">Contraseña</label>
      </div>
      <div class="col-6 col-md-4 col-lg-3">
        <input v-model="password" id="pass" type="password" maxlength="30">
      </div>
    </div>
    <div class="row justify-content-center">
      <div class="col-6 col-md-4 col-lg-3 text-right">
        <label for="rpass" class="letra">Repita la Contraseña</label>
      </div>
      <div class="col-6 col-md-4 col-lg-3">
        <input v-model="rpassword" id="rpass" type="password" maxlength="30">
      </div>
    </div>
    <div class="row boton-ingresar">
      <button @click="register" class="btn btn-lg btn-success">Registrarme</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Register",
  data() {
    return {
      nick: "",
      password: "",
      rpassword: "",
    }
  },
  methods: {
    register() {
      if (this.password && this.rpassword && this.password === this.rpassword) {
        let data = {
          nick: this.nick,
          password: this.password,
        }
        this.$store.dispatch('register', data);
      } else {
        this.$noty.error("Las contraseñas no son iguales");
      }
    }
  }
}
</script>
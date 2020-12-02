<template>
  <div class="col">
    <div class="row justify-content-start">
      <div class="col-6 col-md-4 col-lg-3 text-right">
        <label for="nick" class="letra">Elija su Usuario</label>
      </div>
      <div class="col-6 col-md-4 col-lg-3">
        <input v-model="nick" id="nick" class="mdc-rounded" type="text" maxlength="30" minlength="3">
      </div>
    </div>
    <div class="row justify-content-start">
      <div class="col-6 col-md-4 col-lg-3 text-right">
        <label for="pass" class="letra">Contraseña</label>
      </div>
      <div class="col-6 col-md-4 col-lg-3">
        <input v-model="password" id="pass" class="mdc-rounded" type="password" maxlength="30" minlength="6">
      </div>
    </div>
    <div class="row justify-content-start">
      <div class="col-6 col-md-4 col-lg-3 text-right">
        <label for="rpass" class="letra">Repita la Contraseña</label>
      </div>
      <div class="col-6 col-md-4 col-lg-3">
        <input v-model="rpassword" id="rpass" class="mdc-rounded" type="password" maxlength="30" minlength="6">
      </div>
    </div>
    <div class="row">
      <div  v-if="!validNick" class="col-12 col-md-8 col-lg-6 justify-content-start game-info-div">
        <p class="invalid-message" >El usuario tiene que tener al menos 3 caracteres</p>
      </div>

      <div  v-if="!validPassword" class="col-12 col-md-8 col-lg-6 justify-content-start game-info-div">
        <p class="invalid-message">La contraseña tiene que tener al menos 6 caracteres</p>
      </div>

      <div v-if="!validRPassword" class="col-12 col-md-8 col-lg-6 justify-content-start game-info-div">
        <p class="invalid-message">La contraseña repetida tiene que tener al menos 6 caracteres</p>
      </div>

      <div  v-if="passwordsDoNotmatch" class="col-12 col-md-8 col-lg-6 justify-content-start game-info-div">
        <p class="invalid-message">Las contraseñas no coinciden</p>
      </div>
    </div>

    <div class="row justify-content-start">
      <div class="boton-ingresar col-12 col-md-4 offset-md-4 col-lg-3 offset-lg-3">
        <button @click="register" class="btn btn-lg btn-success" :disabled="anyFieldInvalid">Registrarme</button>
      </div>
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
  computed: {
    anyFieldInvalid() {
      return !this.validNick || !this.validPassword || !this.validRPassword || this.passwordsDoNotmatch;
    },
    validNick() {
      return this.nick.length >= 3 || this.nick.length === 0;
    },
    validPassword() {
      return this.password.length >= 6|| this.password.length === 0;
    },
    validRPassword() {
      return this.rpassword.length >= 6|| this.rpassword.length === 0;
    },
    passwordsDoNotmatch() {
      return this.password !== this.rpassword;
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
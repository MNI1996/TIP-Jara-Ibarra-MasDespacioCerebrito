<template>
  <div class="col-12">
    <div class="row">
      <div class="col-12 light-slate-panel">
        <h2>Registrese</h2>
      </div>
    </div>
    <div class="row login-row">
      <div class="col-5 col-xl-6 text-right">
        <label for="nick" class="letra">Elija su Usuario</label>
      </div>
      <div class="col-7 col-xl-6">
        <input v-model="nick" id="nick" class="mdc-rounded" type="text" maxlength="30" minlength="3">
      </div>
    </div>
    <div class="row login-row">
      <div class="col-5 col-xl-6 text-right">
        <label for="pass" class="letra">Contraseña</label>
      </div>
      <div class="col-7 col-xl-6">
        <input v-model="password" id="pass" class="mdc-rounded" type="password" maxlength="30" minlength="6">
      </div>
    </div>
    <div class="row">
      <div class="col-5 col-xl-6 text-right">
        <label for="rpass" class="letra">Repita la Contraseña</label>
      </div>
      <div class="col-7 col-xl-6">
        <input v-model="rpassword" id="rpass" class="mdc-rounded" type="password" maxlength="30" minlength="6">
      </div>
    </div>
    <div class="row">
      <div v-if="invalidNick" class="col-12 invalid-wrapper">
        <p class="invalid-message">El usuario tiene que tener al menos 3 caracteres</p>
      </div>

      <div v-if="invalidPassword" class="col-12 invalid-wrapper">
        <p class="invalid-message">La contraseña tiene que tener al menos 6 caracteres</p>
      </div>

      <div v-if="invalidRPassword" class="col-12 invalid-wrapper">
        <p class="invalid-message">La contraseña repetida tiene que tener al menos 6 caracteres</p>
      </div>

      <div v-if="passwordNotMatch" class="col-12 invalid-wrapper">
        <p class="invalid-message">Las contraseñas no coinciden</p>
      </div>
    </div>

    <div class="row">
      <div class="boton-ingresar col-12">
        <button @click="register" class="btn btn-lg btn-success">Registrarme</button>
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
      invalidNick: false,
      invalidPassword: false,
      invalidRPassword: false,
      passwordNotMatch: false,
    }
  },
  computed: {
    anyFieldInvalid() {
      return !this.validNick || !this.validPassword || !this.validRPassword || !this.passwordsMatch;
    },
    validNick() {
      return this.nick.length >= 3;
    },
    validPassword() {
      return this.password.length >= 6;
    },
    validRPassword() {
      return this.rpassword.length >= 6;
    },
    passwordsMatch() {
      return this.password === this.rpassword;
    }
  },
  methods: {
    register() {
      this.invalidNick = !this.validNick
      this.invalidPassword = !this.validPassword;
      this.invalidRPassword = !this.validRPassword;
      this.passwordNotMatch = !this.passwordsMatch;
      if (this.anyFieldInvalid) {
        return;
      }
      let data = {
        nick: this.nick,
        password: this.password,
      }
      this.$store.dispatch('register', data);
    }
  }
}
</script>
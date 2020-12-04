<template>
  <div class="col-12">
    <div class="row">
      <div class="col-12 light-slate-panel">
        <h2>Inicie Sesión</h2>
      </div>
    </div>
    <div class="row login-row">
      <div class="col-5 col-xl-4 text-right">
        <label for="nick" class="login-label">Usuario</label>
      </div>
      <div class="col-7 col-xl-7">
        <input v-model="nick" class="mdc-rounded" id="nick" type="text" maxlength="30" minlength="3">
      </div>
    </div>
    <div class="row login-row">
      <div class="col-5 col-xl-4 text-right">
        <label for="pass" class="login-label">Contraseña</label>
      </div>
      <div class="col-7 col-xl-7">
        <input v-model="password" id="pass" class="mdc-rounded" type="password" maxlength="30" minlength="6">
      </div>
    </div>
    <div class="row">
      <div v-if="invalidNick" class="col-12 invalid-wrapper">
        <p class="invalid-message" >El usuario tiene que tener al menos 3 caracteres</p>
      </div>
      <div v-if="invalidPassword" class="col-12 invalid-wrapper">
        <p class="invalid-message" >La contraseña tiene que tener al menos 6 caracteres</p>
      </div>

    </div>
    <div class="boton-ingresar col-12">
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
      invalidNick: false,
      invalidPassword: false,
    }
  },
  computed:{
    anyFieldInvalid(){
      return !this.validNick || !this.validPassword
    },
    validNick(){
      return this.nick.length >= 3;
    },
    validPassword(){
      return this.password.length >= 6;
    },
  },
  methods: {
    login() {
      this.invalidNick = !this.validNick
      this.invalidPassword = !this.validPassword;
      if(this.anyFieldInvalid){
        return ;
      }
      let data = {
        nick: this.nick,
        password: this.password,
      }
      this.$store.dispatch('login', data);
    }
  }
}
</script>
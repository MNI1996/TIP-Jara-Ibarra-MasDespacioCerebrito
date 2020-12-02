<template>
  <div class="col">
    <div class="row justify-content-start " >
      <div class="col-6 col-md-4 col-lg-3 text-right">
        <label for="nick" class="letra">Usuario</label>
      </div>
      <div class="col-6 col-md-4 col-lg-3">
        <input v-model="nick" class="mdc-rounded" id="nick" type="text" maxlength="30" minlength="3">
      </div>
    </div>
    <div class="row justify-content-start ">
      <div class="col-6 col-md-4 col-lg-3 text-right">
        <label for="pass" class="letra">Contraseña</label>
      </div>
      <div class="col-6 col-md-4 col-lg-3">
        <input v-model="password" id="pass" class="mdc-rounded" type="password" maxlength="30" minlength="6">
      </div>
    </div>
    <div class="row ">
      <div v-if="!validNick" class="col-12 col-md-8 col-lg-6 justify-content-start game-info-div">
        <p class="invalid-message" >El usuario tiene que tener al menos 3 caracteres</p>

      </div>
      <div v-if="!validPassword" class="col-12 col-md-8 col-lg-6 justify-content-start game-info-div">
        <p class="invalid-message" >La contraseña tiene que tener al menos 6 caracteres</p>
      </div>

    </div>
    <div class="boton-ingresar col-12 col-md-4 offset-md-4 col-lg-3 offset-lg-3">
      <button @click="login" class="btn btn-lg btn-success" :disabled="anyFieldInvalid">Ingresar</button>
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
  computed:{
    anyFieldInvalid(){
      return !this.validNick || !this.validPassword
    },
    validNick(){
      return this.nick.length >= 3 || this.nick.length ===0 ;
    },
    validPassword(){
      return this.password.length >= 6 || this.password.length === 0 ;
    },
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
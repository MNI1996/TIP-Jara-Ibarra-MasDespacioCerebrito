<template>
  <div>
    <label style="color: aliceblue">
      Elija su Nombre
      <input v-model="nick" type="text" maxlength="30">
    </label>
    <button @click="login" class="btn btn-lg btn-success">Ingresar</button>
  </div>
</template>

<script>
export default {
  name: "UserLogin",
  data() {
    return {
      nick: "",
    }
  },
  methods:{
    login(){
      this.$store.dispatch('login', this.nick);
    }
  }
}
</script>

<style scoped>

</style>
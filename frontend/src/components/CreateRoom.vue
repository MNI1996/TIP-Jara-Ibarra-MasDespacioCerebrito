<template>
  <div>
    <h1>Create a Room!</h1>
    <button @click="createARoom" class="btn btn-lg btn-success">Create a Room</button>
  </div>
</template>

<script>
export default {
  name: "CreateRoom",
  methods:{
    createARoom(){
      this.$router.push({name: "room"})
    }
  }
}
</script>

<style scoped>

</style>
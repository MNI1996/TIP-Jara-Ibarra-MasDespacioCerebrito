<template>
  <h1>This is rooms</h1>
  <ul >
    <li v-for="room in rooms">
      <div class="row">
        <div class="col-md-8">
      <h3>
        {{room.name}}
      </h3>
        </div>
        <div class="col-md-4">
          <button @click="methods.createRoomConnection()" class="btn btn-lg btn-success">Entrar a la sala</button>
        </div>
      </div>
    </li>
  </ul>
</template>

<script>
export default {
name: "Rooms",

computed:{
  methods: {
    createRoomConnection(){
      this.socket.on('connect', () => {
        // either with send()
        this.socket.send('Hello!');

        // or with emit() and custom event names
        this.socket.emit('my_event', 'Hello!');
      });
    }
  }
}
}

</script>

<style scoped>

</style>
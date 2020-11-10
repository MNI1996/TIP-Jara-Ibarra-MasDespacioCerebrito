<template>
  <div style="width: 100px ;height: 100px;">
    <img src="Images/Profile.png" alt="" class="img-fluid " style="width: 85px;height: 50px">
    <p >{{dato}}</p>
  </div>
</template>

<script>
export default {
name: "UserCard",
  props: {dato:String},
}

</script>

<style scoped>

p{
  font-size: 30px;
  color: aliceblue;
}
div:hover{
  text-decoration: none;
  border-radius: 15px;
  color: #150485;
  background-color: rgba( 178, 222, 236,0.5);
}
</style>
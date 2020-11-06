<template>
  <div style="width: 50% ;height: 50%;">
    <img src="Images/Profile.png" alt="" style="width: 150px;height: 100px;">
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
div {
  vertical-align: center;
  height: 250px;
  width: 300px;
  text-align: center;
}
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
<template>
  <div class="user-card">
    <img src="Images/Profile.png" alt="" class="img-fluid ">
    <p>{{dato}}</p>
  </div>
</template>

<script>
export default {
name: "UserCard",
  props: {dato:String},
}
</script>
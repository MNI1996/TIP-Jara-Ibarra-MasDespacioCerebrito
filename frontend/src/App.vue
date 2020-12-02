<template>
  <div class="container-fluid">
    <navbar/>
    <!-- use router-link component for navigation. -->
    <!-- specify the link by passing the `to` prop. -->
    <!-- `<router-link>` will be rendered as an `<a>` tag by default -->

    <!--<router-link :to="{name: 'rooms'}">Go to Rooms</router-link>-->


    <!-- route outlet -->
    <!-- component matched by the route will render here -->
    <router-view></router-view>
  </div>
</template>

<script>
import Navbar from "./components/Navbar.vue";

export default {
  name: "App",
  components: {Navbar},
  mounted() {
    this.validateUserCookie()
  },
  methods: {
    validateUserCookie() {
      let userCookie = this.$cookies.get('user');
      if (userCookie) {
        let data = {
          nick: userCookie._id,
          password: userCookie.password,
        }
        this.$store.dispatch('login', data);
      }
    }
  }
}
</script>
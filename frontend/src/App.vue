<template>
  <div>
    <div class="row" style="background-color: darkcyan">
      <div class="col-md-2">
        <router-link :to="{name: 'home'}">
          <img src="Images/Logo.png" alt="Brainy" style="width: 100px;height: 75px;">
        </router-link>
      </div>

      <div class="col-md-8">
        <h1>Mas Despacio Cerebrito</h1>
      </div>

      <div class="col-md-2">
        <router-link :to="{name: 'profile'}">
          <img src="Images/Profile.png" alt="" style="height: 50px;width: 65px">
        </router-link>
      </div>

    </div>
    <p>
        <!-- use router-link component for navigation. -->
        <!-- specify the link by passing the `to` prop. -->
        <!-- `<router-link>` will be rendered as an `<a>` tag by default -->

        <!--<router-link :to="{name: 'rooms'}">Go to Rooms</router-link>-->

    </p>
      <!-- route outlet -->
      <!-- component matched by the route will render here -->
      <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "App",
  created() {
    this.$store.dispatch('loadPlayer');
  }
}
</script>
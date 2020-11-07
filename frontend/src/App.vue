<template>
  <div class="container-fluid">
    <div class="row" style="background-color:#150485 ; background-image: url('../Images/background tapestry.png') ;">
      <div class="col-md-2">
        <router-link :to="{name: 'home'}">
          <img src="Images/Logo.png" alt="Brainy" style="width: 100px;height: 75px;">
        </router-link>
      </div>

      <div class="col-md-6">
        <h1 style="color: aliceblue">Mas Despacio Cerebrito</h1>
      </div>

      <div class="col-md-2">
        <router-link :to="{name: 'ranking'}">
          <h1 style="color: aliceblue">Ranking</h1>
        </router-link>
      </div>

      <div class="col-md-2">
        <router-link :to="{name: 'profile'}" v-if="logged">
          <img src="Images/Profile.png" alt="" style="height: 50px;width: 65px">
        </router-link>
      </div>

    </div>
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
import {mapGetters} from "vuex";

export default {
  name: "App",
  computed:{
    ...mapGetters(["logged"]),
  }
}
</script>
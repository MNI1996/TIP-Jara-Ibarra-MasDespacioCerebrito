<template>
  <div class="container-fluid">
    <div class="row" style="background-color:#150485 ; background-image: url('../Images/background tapestry.png') ;">
      <div class="col col-4" >
        <router-link :to="{name: 'home'}">
          <img src="Images/Logo.png" alt="Brainy" style="width: 17%;" class="img-fluid">
        </router-link>
      </div>
      <div class="col-4">
        <h3 >Mas Despacio Cerebrito</h3>
      </div>

      <div class="col col-2" >
        <router-link :to="{name: 'ranking'}" v-if="logged">
          <!--<button class="btn btn-lg btn-success btn-block" style="width: 100%"></button>-->
            <img src="Images/rank.png" alt="Ranking"  style="width: 35%" class="img-fluid">
        </router-link>
      </div>

      <div class="col col-2">
        <router-link :to="{name: 'profile'}" v-if="logged">
          <img src="Images/Profile.png" alt="Perfil" style="width: 35%" class="img-fluid">
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
<template>
  <div class="container-fluid">
    <div class="row navbar navbar-mdc">
      <div class="row d-sm-none" v-if="logged">
        <div class="col col-4">
          <router-link :to="{name: 'home'}">
            <svg width="50%" viewBox="0 0 16 16" class="bi bi-house-door-fill" fill="white"
                 xmlns="http://www.w3.org/2000/svg">
              <path
                  d="M6.5 10.995V14.5a.5.5 0 0 1-.5.5H2a.5.5 0 0 1-.5-.5v-7a.5.5 0 0 1 .146-.354l6-6a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 .146.354v7a.5.5 0 0 1-.5.5h-4a.5.5 0 0 1-.5-.5V11c0-.25-.25-.5-.5-.5H7c-.25 0-.5.25-.5.495z"/>
              <path fill-rule="evenodd" d="M13 2.5V6l-2-2V2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5z"/>
            </svg>
          </router-link>
        </div>
        <div class="col col-4">
          <router-link :to="{name: 'ranking'}">
            <svg width="50%" viewBox="0 0 16 16" class="bi bi-trophy-fill" fill="white"
                 xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd"
                    d="M2.5.5A.5.5 0 0 1 3 0h10a.5.5 0 0 1 .5.5c0 .538-.012 1.05-.034 1.536a3 3 0 1 1-1.133 5.89c-.79 1.865-1.878 2.777-2.833 3.011v2.173l1.425.356c.194.048.377.135.537.255L13.3 15.1a.5.5 0 0 1-.3.9H3a.5.5 0 0 1-.3-.9l1.838-1.379c.16-.12.343-.207.537-.255L6.5 13.11v-2.173c-.955-.234-2.043-1.146-2.833-3.012a3 3 0 1 1-1.132-5.89A33.076 33.076 0 0 1 2.5.5zm.099 2.54a2 2 0 0 0 .72 3.935c-.333-1.05-.588-2.346-.72-3.935zm10.083 3.935a2 2 0 0 0 .72-3.935c-.133 1.59-.388 2.885-.72 3.935z"/>
            </svg>
          </router-link>
        </div>

        <div class="col col-4">
          <router-link :to="{name: 'profile'}">
            <svg width="50%" viewBox="0 0 16 16" class="bi bi-person-fill" fill="white"
                 xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
            </svg>
          </router-link>
        </div>
      </div>

      <div class="col-12 d-sm-none">
        <img src="Images/logonombre.png" alt="Brainy" class="img-fluid">
      </div>

      <div :class="{'col-12': !logged}" class="col-7 d-none d-sm-block">
        <img src="Images/logonombre.png" alt="Brainy" class="img-fluid">
      </div>

      <div class="col-5 d-none d-sm-block" v-if="logged">
        <div class="col-12 row">
          <div class="col-3">
            <router-link :to="{name: 'home'}">
              <svg width="50%" viewBox="0 0 16 16" class="bi bi-house-door-fill" fill="white"
                   xmlns="http://www.w3.org/2000/svg">
                <path
                    d="M6.5 10.995V14.5a.5.5 0 0 1-.5.5H2a.5.5 0 0 1-.5-.5v-7a.5.5 0 0 1 .146-.354l6-6a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1 .146.354v7a.5.5 0 0 1-.5.5h-4a.5.5 0 0 1-.5-.5V11c0-.25-.25-.5-.5-.5H7c-.25 0-.5.25-.5.495z"/>
                <path fill-rule="evenodd" d="M13 2.5V6l-2-2V2.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5z"/>
              </svg>
            </router-link>
          </div>
          <div class="col-3">
            <router-link :to="{name: 'ranking'}">
              <svg width="50%" viewBox="0 0 16 16" class="bi bi-trophy-fill" fill="white"
                   xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd"
                      d="M2.5.5A.5.5 0 0 1 3 0h10a.5.5 0 0 1 .5.5c0 .538-.012 1.05-.034 1.536a3 3 0 1 1-1.133 5.89c-.79 1.865-1.878 2.777-2.833 3.011v2.173l1.425.356c.194.048.377.135.537.255L13.3 15.1a.5.5 0 0 1-.3.9H3a.5.5 0 0 1-.3-.9l1.838-1.379c.16-.12.343-.207.537-.255L6.5 13.11v-2.173c-.955-.234-2.043-1.146-2.833-3.012a3 3 0 1 1-1.132-5.89A33.076 33.076 0 0 1 2.5.5zm.099 2.54a2 2 0 0 0 .72 3.935c-.333-1.05-.588-2.346-.72-3.935zm10.083 3.935a2 2 0 0 0 .72-3.935c-.133 1.59-.388 2.885-.72 3.935z"/>
              </svg>
            </router-link>
          </div>

          <div class="col-3">
            <router-link :to="{name: 'profile'}">
              <svg width="50%" viewBox="0 0 16 16" class="bi bi-person-fill" fill="white"
                   xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd"
                      d="M3 14s-1 0-1-1 1-4 6-4 6 3 6 4-1 1-1 1H3zm5-6a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/>
              </svg>
            </router-link>
          </div>

        </div>
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
  computed: {
    ...mapGetters(["logged"]),
  }
}
</script>
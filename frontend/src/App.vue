<template>
  <div>
      <h1>Hello App!</h1>
      <p>
        <!-- use router-link component for navigation. -->
        <!-- specify the link by passing the `to` prop. -->
        <!-- `<router-link>` will be rendered as an `<a>` tag by default -->
        <router-link :to="{name: 'home'}">Go to Home</router-link>
        <router-link :to="{name: 'rooms'}">Go to Rooms</router-link>
        <router-link :to="{name: 'profile'}">Go to Profile</router-link>
      </p>
      <!-- route outlet -->
      <!-- component matched by the route will render here -->
      <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "App"
}
</script>
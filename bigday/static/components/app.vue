<template>
  <v-app>
    <v-content>
      <User/>
    </v-content>
  </v-app>
</template>

<script>
import User from "./components/User"

export default {
  name: "App",
  components: {
    User
  }
}
</script>
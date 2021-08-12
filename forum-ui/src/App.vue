<template>
  <v-app>
    <v-main>
      <router-view />
    </v-main>

    <v-footer app>
    <!-- -->
    </v-footer>
  </v-app>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: 'App',
  setup() {
    return {}
  },
})
</script>

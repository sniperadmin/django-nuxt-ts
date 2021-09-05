<template>
  <v-container fluid>
    <v-row align="center" justify="center">
      <v-col cols="8">
        <v-card tile>
          <v-img height="100%" src="https://cdn.vuetifyjs.com/images/cards/server-room.jpg">
            <v-row align="end" class="fill-height cover">
              <v-col align-self="start" class="pa-0" cols="12">
                <v-avatar class="profile" color="grey" size="200" tile>
                  <v-img src="https://cdn.vuetifyjs.com/images/profiles/marcus.jpg"></v-img>
                </v-avatar>
              </v-col>

              <v-col class="py-0">
                <v-list-item color="rgba(0, 0, 0, .4)" dark>
                  <v-list-item-content>
                    <v-list-item-title class="text-h6">
                      {{ $auth.user.first_name }}
                    </v-list-item-title>
                    <v-list-item-subtitle>Network Engineer</v-list-item-subtitle>
                  </v-list-item-content>
                </v-list-item>
              </v-col>
            </v-row>
          </v-img>
        </v-card>
      </v-col>

      <v-col>
        information
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
  import {
    defineComponent,
    ref
  } from "@nuxtjs/composition-api";
  export default defineComponent({
    name: 'Profile',

    setup(props, context) {


      return {}
    }
  });

</script>

<style scoped>
.cover {
  background: linear-gradient(180deg, rgba(2,0,36,1) 0%, rgba(108,108,114,0.28333340172006305) 83%);
}
</style>

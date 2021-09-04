<template>
  <v-app dark>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant="miniVariant"
      :clipped="clipped"
      fixed
      app
    >
      <v-list>
        <v-list-item
          v-for="(item, i) in filteredItems"
          :key="i"
          :to="item.to"
          router
          exact
        >
          <v-list-item-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>

        <v-list-item link v-if="$auth.loggedIn" @click="logout">
          <v-list-item-action>
            <v-icon>mdi-power-off</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            Logout
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-app-bar
      :clipped-left="clipped"
      fixed
      app
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-btn
        icon
        @click.stop="miniVariant = !miniVariant"
      >
        <v-icon>mdi-{{ `chevron-${miniVariant ? 'right' : 'left'}` }}</v-icon>
      </v-btn>
      <v-btn
        icon
        @click.stop="clipped = !clipped"
      >
        <v-icon>mdi-application</v-icon>
      </v-btn>
      <v-btn
        icon
        @click.stop="fixed = !fixed"
      >
        <v-icon>mdi-minus</v-icon>
      </v-btn>
      <v-toolbar-title v-text="title" />
      <v-spacer />
      <v-btn
        icon
        @click.stop="rightDrawer = !rightDrawer"
      >
        <v-icon>mdi-menu</v-icon>
      </v-btn>
    </v-app-bar>
    <v-main>
      <v-container>
        <v-alert :type="$auth.loggedIn ? 'success' : 'error'">
          Logged in status => {{ $auth.loggedIn }}
        </v-alert>
        <Nuxt />
      </v-container>
    </v-main>
    <v-navigation-drawer
      v-model="rightDrawer"
      :right="right"
      temporary
      fixed
    >
      <v-list>
        <v-list-item @click.native="right = !right">
          <v-list-item-action>
            <v-icon light>
              mdi-repeat
            </v-icon>
          </v-list-item-action>
          <v-list-item-title>Switch drawer (click me)</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-footer
      :absolute="!fixed"
      app
    >
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
  </v-app>
</template>

<script lang="ts">
import { defineComponent, ref, reactive, computed, useContext } from '@nuxtjs/composition-api';

export default defineComponent({
  name: 'Default',
  setup() {
    const clipped = ref(false)
    const drawer = ref(true)
    const fixed = ref(false)
    const miniVariant = ref(false)
    const right = ref(true)
    const rightDrawer = ref(false)
    const title = ref('Vuetify.js')

    const items = ref([
      {
        icon: 'mdi-apps',
        title: 'Welcome',
        to: '/',
        bind: false
      },
      {
        icon: 'mdi-chart-bubble',
        title: 'Inspire',
        to: '/inspire',
        bind: false
      },
      {
        icon: 'mdi-login',
        title: 'Login',
        to: '/auth/login',
        bind: true
      },
      {
        icon: 'mdi-account',
        title: 'Register',
        to: '/auth/register',
        bind: true
      },
    ])

    const { $auth } = useContext()

    const filteredItems = computed(() => {
      const meow = items.value.filter(({ bind }) => !bind || (!$auth.loggedIn && bind))
      console.log(meow);
      return meow
    })

    const logout = () => {
      $auth.logout()
    }

    return {
      clipped,
      drawer,
      fixed,
      miniVariant,
      right,
      rightDrawer,
      title,
      logout,
      filteredItems
    }
  }
})
</script>

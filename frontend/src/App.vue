<template>
  <v-app id="app">
    <!-- <v-app-bar
      v-if="$route.name != 'DiningDashboard'"
    >
      <div>
        <v-app-bar-nav-icon color="white" class="mt-1" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

        <v-toolbar-title class="mt-2">DineRight</v-toolbar-title>
      </div>

      <div style="float: right;" v-if="user">
        <img :src="user.profile_pic" style="border-radius: 50%; width: 40px;">
      </div>
    </v-app-bar> -->
    <div style="height: 60px;"
    v-if="$route.name != 'DiningDashboard'">
    <v-app-bar
      dark
      style="background: #90ACE0;"
      v-if="$route.name != 'DiningDashboard'"
    >
      <v-app-bar-nav-icon @click="drawer = true"></v-app-bar-nav-icon>

      <v-toolbar-title>DineRight</v-toolbar-title>

      <v-spacer></v-spacer>
      <div v-if="user">
        <img :src="user.profile_pic" style="border-radius: 50%; width: 40px;">
      </div>
    </v-app-bar>
    </div>

    <v-navigation-drawer
      v-model="drawer"
      absolute
      temporary
    >
      <v-list
        nav
        dense
      >
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
          <v-list-item>
            <v-list-item-title><router-link class="link" to="/student">Dashboard</router-link></v-list-item-title>
          </v-list-item>
  
          <v-list-item>
            <v-list-item-title><router-link class="link" to="/studentsignin">Sign In</router-link></v-list-item-title>
          </v-list-item>

          <v-list-item>
            <v-list-item-title><router-link class="link" to="/studentsignup">Sign Up</router-link></v-list-item-title>
          </v-list-item>

        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
    <router-view />
  </v-app>
</template>

<style lang="css">
@import url('https://fonts.googleapis.com/css?family=Roboto&display=swap');
@import url('https://fonts.googleapis.com/css?family=Poppins&display=swap');

:root {
  --main-font: 'Poppins';
  --main-blue: #90ACE0;
  --main-yellow: #FCD47C;
  --main-gray: #F9F9F9;
}

.mainfont {
  font-family: var(--main-font);
}

#app {
  font-family: var(--main-font);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.link {
  text-decoration: none;
  color: var(--main-blue);
}

</style>

<script>
import { state } from './utils';

export default {
  name: 'App',

  components: {
    
  },

  created() {
    
  },

  mounted() {
    state.addCallback('user_set', () => {
      this.user = state.get('user');
    });
  },

  watch: {
    group () {
        this.drawer = false
      },
  },

  data() {
    return {
      drawer: false,
      group: null,
      user: null,
    }
  },

  computed: {
  },

  methods: {
    
  },
}
</script>


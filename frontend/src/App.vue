<template>
  <v-app id="app">
    <div
      style="background-color: #90ACE0; color: white; height: 50px; display: flex; justify-content: flex-start;"
      v-if="$route.name != 'DiningDashboard'"
    >
      <v-app-bar-nav-icon color="white" class="mt-1" @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title class="mt-2">DineRight</v-toolbar-title>

    </div>

    <v-navigation-drawer
      v-model="drawer"
      absolute
      bottom
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
            <v-list-item-title><router-link to="/student">Dashboard</router-link></v-list-item-title>
          </v-list-item>


        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <router-view/>
  </v-app>
</template>

<style lang="scss">
@import url('https://fonts.googleapis.com/css? family=Oxygen:300,400,700&display=swap');
@import url('https://fonts.googleapis.com/css? family=Comfortaa&display=swap');
@import url('https://fonts.googleapis.com/css?family=Noto+Sans&display=swap');
@import url('https://fonts.googleapis.com/css?family=Roboto&display=swap');
@import url('https://fonts.googleapis.com/css?family=Poppins&display=swap');
@import url('https://fonts.googleapis.com/css?family=Lato&display=swap');

:root {
  --main-font: 'Poppins';
  --main-blue: #90ACE0;
  --main-yellow: #FCD47C;
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


</style>

<script>

export default {
  name: 'App',

  components: {
    
  },

  created() {
    
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
    }
  },

  computed: {
  },

  methods: {
    
  },
}
</script>


<template>
  <v-app id="app">
    <v-app-bar
      color="blue"
      dark
      v-if="$route.name != 'DiningDashboard'"
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>DineRight</v-toolbar-title>

    </v-app-bar>

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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
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


<template>
  <div>
  <v-card
    :loading="loading"
    class="mx-auto my-12"
    max-width="374"
  >
    <template slot="progress">
      <v-progress-linear
        color="deep-purple"
        height="10"
        indeterminate
      ></v-progress-linear>
    </template>

    <v-img
      height="250"
      src="https://i2.wp.com/www.dailycal.org/assets/uploads/2016/11/patz_mikaelaRaphael_staff-900x580.jpg"
    ></v-img>

    <v-card-title>CROSSROADS</v-card-title>

    <v-card-text>
      <v-row
        align="center"
        class="mx-0"
        style="margin-bottom: -5px;"
      >
        <v-chip-group
          column
        >
          <v-chip
          class="mr-2"
          color="red"
          text-color="white"
          ><div class="blink" style="height: 10px; width: 10px; border-radius: 50%; background-color: white;"></div>
          <div class="amber--text ml-1">
            4.5 (54)
          </div>
          <v-rating
            :value="4.5"
            color="amber"
            dense
            half-increments
            readonly
            size="14"
            class="ml-1"
          ></v-rating>
          </v-chip>
<v-dialog
      v-model="dialog"
      width="500"
    >
      <template v-slot:activator="{ on, attrs }">
          <v-chip v-bind="attrs"
          v-on="on"
          color="var(--main-yellow)">10 friends</v-chip>
      </template>

      <v-card>
        <v-card-title class="grey lighten-2" style="font-family: var(--main-font);">
          Friends at Crossroads
        </v-card-title>

        <v-card-text>
          <v-banner
            single-line
            @click:icon="alert"
          >
            <v-avatar><img
              src="https://cdn.vuetifyjs.com/images/john.jpg"
              alt="John"
            ></v-avatar>
            Tony Xin
            
            <v-spacer></v-spacer>
            <p>What's up dawg</p>
          </v-banner>
        </v-card-text>
      </v-card>
    </v-dialog>
        </v-chip-group>
      </v-row>

      <v-chip-group
        v-model="selection"
        active-class="deep-purple accent-4 white--text"
        column
      >
        <v-chip>10:30 AM - 9:00 PM</v-chip>
        <v-chip>5:30 PM - 9:00 PM</v-chip>
      </v-chip-group>
    </v-card-text>
  </v-card>

  
  </div>
</template>

<style scoped>
  .blink {
    animation: blink-animation 1s steps(30, start) infinite;
    -webkit-animation: blink-animation 1s steps(30, start) infinite;
    transition: 0.1s all;
  }
  @keyframes blink-animation {
    to {
      opacity: 0.0;
    }
  }
  @-webkit-keyframes blink-animation {
    to {
      opacity: 1.0;
    }
  }
</style>

<script>

export default {
  name: 'StudentCafeCard',
  components: {
      
  },

  created() {
    
  },

  watch: {
      
  },

  data() {
    return {
      dialog: false,
    }
  },

  computed: {
  },

  methods: {
    
  },

}
</script>

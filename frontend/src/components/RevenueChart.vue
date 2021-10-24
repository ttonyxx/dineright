<template>
<v-container style = "margin-left: -100px;">

  <v-card
    class="mx-auto text-center"
    color="white"
    dark
    max-width="600"
  >
    <v-card-text>
      <v-sheet color="white">
        <v-sparkline
          :value="value"
          color="var(--main-yellow)"
          height="100"
          padding="24"
          stroke-linecap="round"
          auto-draw
          smooth
        >
          <template v-slot:label="item">
            {{ item.value }}
          </template>
        </v-sparkline>
      </v-sheet>
    </v-card-text>

    <v-card-text style = "color: var(--main-yellow)">
      <div class="text-h4 font-weight-thin" style = "color: -var(--main-yellow)">
        Weekly Revenue
      </div>
    </v-card-text>

    <v-divider></v-divider>

    <v-card-actions class="justify-center" style = "color: var(--main-yellow)">
      <v-btn
        block
        text
        style = "color: var(--main-yellow)"
      >
        Go to Report
      </v-btn>
    </v-card-actions>
  </v-card>
</v-container>
</template>

<script>


export default {
  name: 'RevenueChart',
  components: {
  },

  created() {
    
  },

  watch: {

  },

  data() {
    return {
        value: [423*14,
        446*14,
        675*14,
        510*14,
        590*14,
        610*14,
        760*14]
    }
  },

  computed: {
  },

  methods: {
    
  },

}
</script>

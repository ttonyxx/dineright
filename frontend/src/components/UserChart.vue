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
          color="var(--main-blue)"
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

    <v-card-text style = "color: var(--main-blue)">
      <div class="text-h4 font-weight-thin" style = "color: -var(--main-blue)">
        Weekly Visitors
      </div>
    </v-card-text>

    <v-divider></v-divider>

    <v-card-actions class="justify-center" style = "color: var(--main-blue)">
      <v-btn
        block
        text
        style = "color: var(--main-blue)"
      >
        Go to Report
      </v-btn>
    </v-card-actions>
  </v-card>
</v-container>
</template>

<script>


export default {
  name: 'UserChart',
  components: {
  },

  created() {
    
  },

  watch: {

  },

  data() {
    return {
        value: [423,
        446,
        675,
        510,
        590,
        610,
        760]
    }
  },

  computed: {
  },

  methods: {
    
  },

}
</script>

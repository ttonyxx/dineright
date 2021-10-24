<template>
  <v-list-item style="width: 350px;">
    <v-list-item-content style="font-family: var(--main-font);">
      <v-row align="left">
        <v-col cols="auto" class="py-0 pr-0" style="margin-left: 0px;" align="left">
          <v-list-item-title style="margin-top: 15px; width: 10000000px"><v-chip class="mr-1">13g Protein | 5g Fat | 260 Calories</v-chip> </v-list-item-title>
        </v-col>

      </v-row>
    </v-list-item-content>

    <v-list-item-action>
      
    </v-list-item-action>
  </v-list-item>
</template>

<script>
export default {
  name: 'Nutrition',
  props: {
    nutritionalfacts: {type: Object, required: true},
  },
  data() {
    return {
    }
  },
  computed: {
  },
  methods: {
  },
}
</script>
<template>
  <v-container class="diningdashboard text-left text-h2 font-weight-bold" 
  :style = "bgColor"
  fluid>
    <v-row class = "mb-5"
    style = "color: var(--main-blue);"
    >
      {dining_hall} Dashboard
      </v-row>
    <v-spacer class  = "mb-10"></v-spacer>
    <DiningStatsCard> </DiningStatsCard>
    <v-spacer class  = "mb-10"></v-spacer>

    <UserChart></UserChart>
    <v-spacer class  = "mb-10"></v-spacer>

    <UserChart></UserChart>
  </v-container>
</template>

<script>


import DiningStatsCard from '@/components/DiningStatsCard.vue'
import UserChart from '@/components/UserChart.vue'
export default {
  name: 'DiningDashboard',
  components: {
      DiningStatsCard,
      UserChart
  },

  created() {
    
  },

  watch: {

  },

  data() {
    return {
      bgColor: {
        backgroundColor: 'var(--main-gray)',
        height: '140vh'
      }
    }
  },

  computed: {
  },

  methods: {
    
  },

}
</script>

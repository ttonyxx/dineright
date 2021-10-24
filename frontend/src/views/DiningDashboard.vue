<template>
  <v-container class="diningdashboard text-left text-h2 font-weight-bold" 
  :style = "bgColor"
  fluid>
    <v-row class = "mb-5"
    style = "color: #15284B"
    fluid
    >
    <v-col>
      Crossroads Dining Hall Dashboard
    </v-col>
      </v-row>
    <v-spacer class  = "mb-10"></v-spacer>
    <DiningStatsCard> </DiningStatsCard>

    <v-spacer class  = "mb-10"></v-spacer>
    <v-row :align = "align">
      <v-col :style = "bgColor">

          <UserChart></UserChart>
          <RevenueChart></RevenueChart>
      </v-col>
      <v-col>
      <TestCard :items="items"></TestCard>
      <BadFood :items = "worst_items"></BadFood>
    </v-col>
    </v-row>
    
    <v-spacer class  = "mb-10"></v-spacer>

  </v-container>
</template>

<script>


import DiningStatsCard from '@/components/DiningStatsCard.vue'
import UserChart from '@/components/UserChart.vue'
import TestCard from '@/components/TestCard.vue'
import BadFood from '@/components/BadFood.vue'
import RevenueChart from '@/components/RevenueChart.vue'

export default {
  name: 'DiningDashboard',
  components: {
      DiningStatsCard,
      UserChart,
      TestCard,
      BadFood,
      RevenueChart
  },

  created() {
  },

  watch: {
      
  },

  data() {
    return {
      bgColor: {
        backgroundColor: 'var(--main-gray)',
        // marginLeft: '40px',
        height: '140vh',
      },
      items: [
      {
        color: "#FCD47C",
        src: "https://cleanfoodcrush.com/wp-content/uploads/2020/06/Clean-Food-Crush-Healthy-Recipes-Buffalo-Chicken-Salad.jpg",
        menuitem: "Buffalo Chicken Salad",
        description: "Tangy buffalo sauce topped on deep fried chicken",
        rating: 8.5
      },
      {
        color: "#90ACE0",
        src: "https://hips.hearstapps.com/hmg-prod/images/grilled-chicken-horizontal-1532030541.jpg",
        menuitem: "Chicken Breast",
        description: "Oven roasted chicken breast seasoned with traditional Texan spices",
        rating: 8.2
      },
    ],
    worst_items: [
      {
        color: "#E37979",
        src: "https://www.aheadofthyme.com/wp-content/uploads/2016/03/farfalle-pasta-with-light-creamy-mushroom-rose-sauce-01.jpg",
        menuitem: "Rose Pasta",
        description: "Creamy rose pasta with tender mushrooms and farfalle pasta",
        rating: 2.4
      },
      {
        color: "#E37979",
        src: "https://ww2.kqed.org/app/uploads/sites/24/2016/08/IMG_8073.jpg",
        menuitem: "Dumplings",
        description: "Traditional dumplings with soft and chewy shells",
        rating: 3.5
      }
    ]
    }
  },

  computed: {
  },

  methods: {
    
  },

}
</script>

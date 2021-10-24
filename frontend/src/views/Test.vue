<template>
  <v-container class="test">

      <TestCard :items="items"></TestCard>
  
  </v-container>
</template>

<script>
import TestCard from '@/components/TestCard'

export default {
  name: "TestPage",
  components: {
    TestCard,
  },
  data: () => ({
    items: [
      {
        color: "#FCD47C",
        src: "https://cleanfoodcrush.com/wp-content/uploads/2020/06/Clean-Food-Crush-Healthy-Recipes-Buffalo-Chicken-Salad.jpg",
        menuitem: "Buffalo Chicken Salad",
        description: "Tangy buffalo sauce topped on deep fried chicken",
        price: "$11"
      },
      {
        color: "#90ACE0",
        src: "https://hips.hearstapps.com/hmg-prod/images/grilled-chicken-horizontal-1532030541.jpg",
        menuitem: "Chicken Breast",
        description: "Oven roasted chicken breast seasoned with traditional Texan spices",
        price: "$9.50"
      }
    ],
  }),
};
</script>

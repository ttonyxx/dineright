<template>
<v-container>
    <!-- Create vuetify component with centered text  -->




  <v-layout row justify-space-between>
      <v-card width = "360px" height = "120px" align="center" class = "rounded-lg">
          <v-icon class = "mr-10" style="margin-bottom: -40px; color: var(--main-blue);" size = "50">mdi-cash-multiple</v-icon>
        <v-card-title-text style="font-size: 30px; color: var(--main-blue);">
            Revenue
        </v-card-title-text>
        <v-card-text class = "ml-10" style = "font-size: 30px; color: var(--main-yellow);">
            $1945
        </v-card-text>
    </v-card>
<v-card width = "360px" height = "120px" align="center" class = "rounded-lg">
          <v-icon class = "mr-10" style="margin-bottom: -40px; color: var(--main-blue);" size = "50">mdi-currency-usd</v-icon>
        <v-card-title-text style="font-size: 30px; color: var(--main-blue);">
            Expenses
        </v-card-title-text>
        <v-card-text class = "ml-10" style = "font-size: 30px; color: var(--main-yellow);">
            $1945
        </v-card-text>
    </v-card>
    <v-card width = "360px" height = "120px" align="center" class = "rounded-lg">
          <v-icon class = "mr-10" style="margin-bottom: -40px; color: var(--main-blue);" size = "50">mdi-account-multiple-plus-outline</v-icon>
        <v-card-title-text style="font-size: 30px; color: var(--main-blue);">
            New Visitors
        </v-card-title-text>
        <v-card-text class = "ml-10" style = "font-size: 30px; color: var(--main-yellow);">
            $1945
        </v-card-text>
    </v-card>
    <v-card width = "360px" height = "120px" align="center" class = "rounded-lg">
          <v-icon class = "mr-10" style="margin-bottom: -40px; color: var(--main-blue);" size = "50">mdi-timer</v-icon>
        <v-card-title-text style="font-size: 30px; color: var(--main-blue);">
            Avg. Time Stayed
        </v-card-title-text>
        <v-card-text class = "ml-10" style = "font-size: 30px; color: var(--main-yellow);">
            $1945
        </v-card-text>
    </v-card>


  </v-layout>
</v-container>
</template>
<script>
  export default {
    data() {
    return {
    }
  },
  }
</script>
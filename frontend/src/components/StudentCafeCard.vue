<template>
  <div>
  <v-card
    class="mx-auto mt-4"
    max-width="374"
    style="overflow: hidden;"
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
      :src="cafeteria.c.photo"
      @click="$router.push('/crossroads')"
    ></v-img>
    

        <v-tooltip top v-if="cafeteria.c.recommended">
      <template v-slot:activator="{ on, attrs }">
          <div v-bind="attrs"
          v-on="on" style="position: absolute; top: 10px; right: 10px; background-color: #FCD47C; border-radius: 50%; font-size: 3px;"><v-icon color="white">mdi-star</v-icon></div>

      </template>
      <span>DineRight recommended</span>
    </v-tooltip>
      
        <v-card-title>{{cafeteria.c.name}}


          <v-tooltip top>
      <template v-slot:activator="{ on, attrs }">
        <v-chip class="ml-2" color="green lighten-3"
          v-bind="attrs"
          v-on="on"> {{ cafeteria.c.score }}</v-chip>
      </template>
      <span>DineRight generated score</span>
    </v-tooltip>
         </v-card-title>

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
            {{cafeteria.c.rating}} ({{cafeteria.c.numRatings}})
          </div>
          <v-rating
            :value="cafeteria.c.rating"
            color="amber"
            background-color="amber"
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
                color="var(--main-yellow)">{{cafeteria.c.friends.length}} friends</v-chip>
            </template>

            <v-card>
              <v-card-title class="grey lighten-2" style="font-family: var(--main-font);">
                <v-chip color="var(--main-yellow)" style="font-size: 18px; margin-right: 5px;">{{cafeteria.c.friends.length}} friends</v-chip> at Crossroads
              </v-card-title>

              <v-card-text>
                <v-list style="overflow: hidden;">
                  <template v-for="(student, i) in cafeteria.c.friends">
                  <v-divider
                    v-if="i !== 0"
                    :key="i"
                  ></v-divider>
                  <StudentListItem 
                    :key="student.uid"
                    :student="student"
                  />
                </template>
                </v-list>
              </v-card-text>
            </v-card>
          </v-dialog>
          
        </v-chip-group>
      </v-row>

      <v-chip-group
        column
      >
        <v-chip>10:30 AM - 2:30 PM</v-chip>
        <v-chip outlined>5:30 PM - 9:00 PM</v-chip>
      </v-chip-group>

      <v-divider></v-divider>

      <v-row class="px-3 pt-4" style="font-weight: bold;">
        Top menu items
      </v-row>
      <v-row class="pl-3 pb-4 pt-2" style="height: 150px; overflow: scroll;">

          <v-dialog
            v-model="dialogFood"
            width="500"
            v-for="(food, i) in cafeteria.c.foods"
            :key="i"
          >
            <template v-slot:activator="{ on, attrs }">
<div v-bind="attrs"
                v-on="on" class="menu-item">
            {{food.name}}<br>
            <v-img style="display: inline-block; border-radius: 5px;" height="80px" width="80px" :src="food.imageUrl"></v-img>
          </div>
            </template>

            <v-card>
                <v-card-title
                  class="grey lighten-2"
                  style="font-family: var(--main-font)"
                >
                  <v-chip
                    color="var(--main-blue)"
                    style="font-size: 18px; margin-right: 5px"
                    >Nutritional Facts</v-chip
                  >
                </v-card-title>

                <v-card-text>
                  <v-list style="overflow: hidden">
                    <template v-for="(nutritionalfacts, i) in 1">
                      <v-divider v-if="i !== 0" :key="i"></v-divider>
                      <Nutrition :key="nutritionalfacts.uid" :nutritionalfacts="nutritionalfacts" />
                    </template>
                  </v-list>
                </v-card-text>
              </v-card>
          </v-dialog>

      </v-row>
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

  .menu-item {
    background-color: #E3F2FD;
    text-align: center;
    padding: 5px 10px 10px 10px;
    border-radius: 10px;
    margin-right: 10px;
    float: left;
    margin-bottom: 10px;
  }
</style>

<script>
import StudentListItem from '@/components/StudentListItem.vue';
import Nutrition from './Nutrition.vue';

export default {
  name: 'StudentCafeCard',
  components: {
      StudentListItem,
    Nutrition
  },

  created() {
  },

  watch: {
      
  },

  props: {
    cafeteria: {type: Object, required: true},
  },

  data() {
    return {
      dialog: false,
      dialogFood: false
    }
  },

  computed: {
  },

  methods: {
    
  },

}
</script>

<template>
  <div class="crossroads pb-6">

    <v-img :src="cafeteria.photo" max-height="100"
    gradient="to top right, rgba(100,115,201,.33), rgba(25,32,72,.7)"
    ></v-img>

    <h1 style="color: white; position: absolute; top: 100px; left: 10px;">{{ cafeteria.name }}</h1>

    <v-container>
        <v-btn block outlined color="indigo" v-if="!hereNow" @click="hereNow = true">I'm Here Right Now</v-btn>
        <v-expand-transition>
        <div v-if="hereNow" style="background-color: #F5F5F5; padding: 10px; border-radius: 10px;">
          <h2>How is it?</h2>
          <div style="display: flex;">
            <v-chip style="margin: 5px;">
              Crowded?
            </v-chip>
            <v-chip style="margin: 5px;">
              Empty?
            </v-chip>
          </div>
        </div>
        </v-expand-transition>
        <h1 style="font-size: 25px;"><v-icon color="#2C3E50">mdi-chart-areaspline-variant</v-icon> Real-Time Stats</h1>
        
        <div id="stats">
            <h1> Score: <v-chip color="green lighten-3"> {{ cafeteria.score }}</v-chip></h1>

          <h1>People: <v-chip>129 <v-icon>mdi-account</v-icon></v-chip>
            
          <v-dialog
            v-model="dialog"
            width="500"
          >
            <template v-slot:activator="{ on, attrs }">
                <v-chip v-bind="attrs"
                v-on="on"
                color="var(--main-yellow)" class="ml-1">{{cafeteria.friends.length}} <v-icon>mdi-account-multiple</v-icon></v-chip>
            </template>

            <v-card>
              <v-card-title class="grey lighten-2" style="font-family: var(--main-font);">
                <v-chip color="var(--main-yellow)" style="font-size: 18px; margin-right: 5px;">{{cafeteria.friends.length}} friends</v-chip> at Crossroads
              </v-card-title>

              <v-card-text>
                <v-list style="overflow: hidden;">
                  <template v-for="(student, i) in cafeteria.friends">
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
            
            </h1>
            <h1>User Rating:
                <v-chip
          class="mr-2"
          color="red"
          text-color="white"
          > 
          <div class="amber--text ml-1">
            {{cafeteria.rating}} ({{cafeteria.numRatings}})
          </div>
          <v-rating
            :value="cafeteria.rating"
            color="amber"
            background-color="amber"
            dense
            half-increments
            readonly
            size="14"
            class="ml-1"
          ></v-rating>
          </v-chip>
            </h1>
        </div>

        <h1 class="mt-2" style="font-size: 25px;"><v-icon color="#2C3E50"
        >
        mdi-calendar
        </v-icon> Calendar</h1>
        <Calendar class="mt-3 mx-1"></Calendar>

        <h1 class="mt-4" style="font-size: 25px;"><v-icon
        
        color="#2C3E50"
        >
        mdi-message-draw
        </v-icon> Reviews 
        
         <v-dialog
            v-model="dialogReview"
            width="500"
          >
            <template v-slot:activator="{ on, attrs }">
                <v-icon v-bind="attrs"
                v-on="on"
                color="var(--main-yellow)" >mdi-plus-box</v-icon>
            </template>

            <v-card>
              <v-card-title class="grey lighten-2" style="font-family: var(--main-font);">
                Add a review
              </v-card-title>

              <v-card-text>
                <v-btn
                v-if="!photoAdded"
                depressed
                color="var(--main-yellow)"
                class="mt-3"
                @click="photoAdded = true"
                >
                + Photo
                </v-btn>

                <v-container v-if="photoAdded">
                <div style="padding: 1px 8px 8px 8px; border-radius: 5px; background-color: #E0E0E0;">
                <v-img class="mt-4" src="@/assets/review.png"></v-img>
                </div>

                <v-row class="mt-4" style="margin-left: -3px;">
                <h1 style="font-size: 20px;">Pesto Pasta</h1>
                </v-row>
                <v-row>
                    <v-rating
                    v-model="rating"
                    background-color="amber lighten-3"
                    style="margin-top: -5px; margin-left: -2px;"
                    color="amber"
                    half-increments
                    
                    ></v-rating>
                    <v-textarea solo>
                    </v-textarea>
                </v-row>

                <v-row class="mt-4" style="margin-left: -3px;">
                <h1 style="font-size: 20px;">Fish Tacos</h1>
                </v-row>
                <v-row>
                    <v-rating
                    v-model="rating"
                    background-color="amber lighten-3"
                    style="margin-top: -5px; margin-left: -2px;"
                    color="amber"
                    half-increments
                    
                    ></v-rating>
                    <v-textarea solo>
                    </v-textarea>
                </v-row>

                <v-row class="mt-4" style="margin-left: -3px;">
                <h1 style="font-size: 20px;">Caesar Salad</h1>
                </v-row>
                <v-row>
                    <v-rating
                    v-model="rating"
                    background-color="amber lighten-3"
                    style="margin-top: -5px; margin-left: -2px;"
                    color="amber"
                    half-increments
                    
                    ></v-rating>
                    <v-textarea solo>
                    </v-textarea>
                </v-row>

                <v-btn
                color="var(--main-yellow)"
            @click="dialogReview = false; submitted = true;"
                >
                Submit
                </v-btn>
                </v-container>
              </v-card-text>
            </v-card>
          </v-dialog>
        
        </h1>

        <div v-if="submitted">
        <div class="review">
            <h1>Pesto Pasta</h1>
            <v-rating
                    value="5"
                    background-color="amber"
                    style="margin-left: -10px;"
                    color="amber"
                    half-increments
                    
                    ></v-rating>
            <p>Great!</p>
            <v-img height="200px" width="200px" src="@/assets/pestopasta.png"></v-img>
        </div>

        <div class="review">
            <h1>Fish Taco</h1>
            <v-rating
                    value="3"
                    background-color="amber"
                    style="margin-left: -10px;"
                    color="amber"
                    half-increments
                    
                    ></v-rating>
            <p>Kind of bland</p>
            <v-img height="200px" width="200px" src="@/assets/fishtaco.png"></v-img>
        </div>


<div class="review">
            <h1>Caesar Salad</h1>
            <v-rating
                    value="2"
                    background-color="amber"
                    style="margin-left: -10px;"
                    color="amber"
                    half-increments
                    
                    ></v-rating>
            <p>Too salty!</p>
            <v-img height="200px" width="200px" src="@/assets/caesarsalad.png"></v-img>
        </div>

        </div>
        

    </v-container>
  
  </div>
</template>

<style lang="scss" scoped>

.crossroads {
    text-align: left;
}

#stats {
    font-size: 10px;
    margin-top: 10px;

    h1 {
        margin-top: 5px;
    }
}

.review {
    background-color: #F5F5F5;
    border-radius: 10px;
    padding: 10px;
    margin-bottom: 10px;

    h1 {
        font-size: 20px;
    }
}

</style>

<script>
import StudentListItem from '@/components/StudentListItem'
import Calendar from '@/components/Calendar'

export default {
  name: 'Crossroads',
  components: {
      StudentListItem,
      Calendar
  },

  created() {
  },

  watch: {
      
  },

  data() {
    return {
      dialogReview: false,
      photoAdded: false,
      submitted: false,
      hereNow: false,
      cafeterias: [
        {
          name: 'Crossroads',
          score: 8.9,
          rating: 3.57,
          numRatings: 54,
          recommended: true,
          photo: 'https://i2.wp.com/www.dailycal.org/assets/uploads/2016/11/patz_mikaelaRaphael_staff-900x580.jpg',
          students: [
            {
              uid: '21902i192j12',
              first_name: 'Tony',
              last_name: 'Xin',
              photo: 'https://i.imgur.com/HkLY72h.jpg',
              entered: '5:23PM'
            },
            {
              uid: '21902ie3192j12',
              first_name: 'Arjun',
              last_name: 'Patrawala',
              photo: 'https://media-exp1.licdn.com/dms/image/C5603AQHXCZAa5oapJw/profile-displayphoto-shrink_800_800/0/1517630723852?e=1640217600&v=beta&t=g8Hp_-MYGD-tzsiLiLlgQpKulhWppS8OZiKQIQgVmmE',
              entered: '5:34PM',
            },
            {
              uid: '21902i13292j12',
              first_name: 'Chris',
              last_name: 'Chou',
              photo: 'https://media-exp1.licdn.com/dms/image/C4E03AQHbWNkBUotrfg/profile-displayphoto-shrink_800_800/0/1632698333471?e=1640217600&v=beta&t=vYqN7Da1uAMbxm8nOJP0rTKRrx1LW4dZW_Vao17gfXc',
              entered: '5:45PM'
            },
            {
              uid: '21902i1a3292j12',
              first_name: 'Caleb',
              last_name: 'Kim',
              photo: 'https://media-exp1.licdn.com/dms/image/C5603AQFwp44-wj76vw/profile-displayphoto-shrink_800_800/0/1633849143227?e=1640217600&v=beta&t=S85BMzOaqFub7TaefH3-kUmQS2o5lbAFsPCedjUSKZg',
              entered: '5:47PM'
            },
            {
              uid: '21902i1a3292j12',
              first_name: 'Caleb',
              last_name: 'Kim',
              photo: 'https://media-exp1.licdn.com/dms/image/C5603AQFwp44-wj76vw/profile-displayphoto-shrink_800_800/0/1633849143227?e=1640217600&v=beta&t=S85BMzOaqFub7TaefH3-kUmQS2o5lbAFsPCedjUSKZg',
              entered: '5:47PM'
            },
            {
              uid: '21902i1a3292j12',
              first_name: 'Caleb',
              last_name: 'Kim',
              photo: 'https://media-exp1.licdn.com/dms/image/C5603AQFwp44-wj76vw/profile-displayphoto-shrink_800_800/0/1633849143227?e=1640217600&v=beta&t=S85BMzOaqFub7TaefH3-kUmQS2o5lbAFsPCedjUSKZg',
              entered: '5:47PM'
            },
            {
              uid: '21902i1a3292j12',
              first_name: 'Caleb',
              last_name: 'Kim',
              photo: 'https://media-exp1.licdn.com/dms/image/C5603AQFwp44-wj76vw/profile-displayphoto-shrink_800_800/0/1633849143227?e=1640217600&v=beta&t=S85BMzOaqFub7TaefH3-kUmQS2o5lbAFsPCedjUSKZg',
              entered: '5:47PM'
            },
            {
              uid: '21902i1a3292j12',
              first_name: 'Caleb',
              last_name: 'Kim',
              photo: 'https://media-exp1.licdn.com/dms/image/C5603AQFwp44-wj76vw/profile-displayphoto-shrink_800_800/0/1633849143227?e=1640217600&v=beta&t=S85BMzOaqFub7TaefH3-kUmQS2o5lbAFsPCedjUSKZg',
              entered: '5:47PM'
            },
          ],
          friends: [
            {
              uid: '21902i192j12',
              first_name: 'Tony',
              last_name: 'Xin',
              photo: 'https://i.imgur.com/HkLY72h.jpg',
              entered: '5:23PM'
            },
            {
              uid: '21902ie3192j12',
              first_name: 'Arjun',
              last_name: 'Patrawala',
              photo: 'https://media-exp1.licdn.com/dms/image/C5603AQHXCZAa5oapJw/profile-displayphoto-shrink_800_800/0/1517630723852?e=1640217600&v=beta&t=g8Hp_-MYGD-tzsiLiLlgQpKulhWppS8OZiKQIQgVmmE',
              entered: '5:34PM',
            },
            {
              uid: '21902i13292j12',
              first_name: 'Chris',
              last_name: 'Chou',
              photo: 'https://media-exp1.licdn.com/dms/image/C4E03AQHbWNkBUotrfg/profile-displayphoto-shrink_800_800/0/1632698333471?e=1640217600&v=beta&t=vYqN7Da1uAMbxm8nOJP0rTKRrx1LW4dZW_Vao17gfXc',
              entered: '5:45PM'
            },
            {
              uid: '21902i1a3292j12',
              first_name: 'Caleb',
              last_name: 'Kim',
              photo: 'https://media-exp1.licdn.com/dms/image/C5603AQFwp44-wj76vw/profile-displayphoto-shrink_800_800/0/1633849143227?e=1640217600&v=beta&t=S85BMzOaqFub7TaefH3-kUmQS2o5lbAFsPCedjUSKZg',
              entered: '5:47PM'
            },
        ]
        },
        
      ]
    }
  },

  computed: {
      cafeteria() {
          return this.cafeterias[0]
      }
  },

  methods: {
    
  },

}
</script>

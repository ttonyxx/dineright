<template>
  <div class="crossroads">

    <v-img :src="cafeteria.photo" max-height="100"
    gradient="to top right, rgba(100,115,201,.33), rgba(25,32,72,.7)"
    ></v-img>

    <h1 style="color: white; position: absolute; top: 100px; left: 10px;">{{ cafeteria.name }}</h1>

    <v-container>
        <v-btn block outlined color="indigo" v-if="!hereNow" @click="hereNow = true">I'm Here Right Now</v-btn>
        <div v-if="hereNow">
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
        <h1 style="font-size: 25px;"><v-icon color="#2C3E50">mdi-chart-areaspline-variant</v-icon> Real-Time Stats</h1>
        
        <div id="stats">
          <h1>DineRight Score: <v-chip color="green lighten-3"> {{ cafeteria.score }}</v-chip></h1>

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
        </v-icon> Reviews</h1>

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

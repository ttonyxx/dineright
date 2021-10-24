<template>
  <v-container class="studentdashboard">

      <v-row class="pa-2">
      <h1 style="font-size: 22px;">Welcome Tony,</h1>
      <v-spacer></v-spacer>
        <v-chip class="mr-1">5 swipes</v-chip>
        <v-chip>$159.20</v-chip>
      </v-row>

      <StudentCafeCard v-for="(c, i) in cafeterias" :key="i" :cafeteria={c}></StudentCafeCard>
  
  </v-container>
</template>

<script>
import StudentCafeCard from '@/components/StudentCafeCard'

export default {
  name: 'StudentDashboard',
  components: {
      StudentCafeCard
  },

  created() {
  },

  watch: {
      
  },

  mounted() {
    setInterval(() => {
      if (Math.random() < .2) {
        this.cafeterias[0].numRatings += Math.floor((Math.random() * 2)) + 1;
        let newV = (Math.random() * .2 - .1) + this.cafeterias[0].rating;
        this.cafeterias[0].rating = Math.round(newV * 100) / 100;
      }
    }, 1000);
  },

  data() {
    return {
      cafeterias: [
        {
          name: 'Crossroads',
          score: 8.9,
          rating: 3.51,
          numRatings: 54,
          recommended: true,
          photo: 'https://i2.wp.com/www.dailycal.org/assets/uploads/2016/11/patz_mikaelaRaphael_staff-900x580.jpg',
          link: '/crossroads',
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
            }
          ]
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

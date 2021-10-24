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
          foods: [
            {
              name: 'Cheeseburger',
              imageUrl: 'https://www.throwbacks.com/content/images/2018/02/cheeseburger---TripAdvisor.jpg'
            },
            {
              name: 'Macaroni',
              imageUrl: 'https://www.foodiecrush.com/wp-content/uploads/2017/10/Instant-Pot-Macaroni-and-Cheese-foodiecrush.com-019.jpg'
            },
            {
              name: 'Salmon',
              imageUrl: 'https://www.paleorunningmomma.com/wp-content/uploads/2019/11/salmon-primewaters-4.jpg'
            }
          ],
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
        },
        {
          name: 'Café 3',
          score: 7.4,
          rating: 3,
          numRatings: 44,
          recommended: false,
          photo: 'https://news.berkeley.edu/wp-content/uploads/2016/08/kosher-and-halal-cafe.jpg',
          link: '/crossroads',
          foods: [
            {
              name: 'Chicken',
              imageUrl: 'https://hips.hearstapps.com/hmg-prod/images/grilled-chicken-horizontal-1532030541.jpg'
            },
            {
              name: 'Fries',
              imageUrl: 'https://recipes.net/wp-content/uploads/2020/04/copycat-chick-fil-a-waffle-fries.jpeg'
            },
            {
              name: 'Chowder',
              imageUrl: 'https://handletheheat.com/wp-content/uploads/2014/09/New-England-Clam-Chowder-02.jpg'
            }
          ],
          students: [
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
          ]
        },
        {
          name: 'Clark Kerr',
          score: 8.1,
          rating: 4.5,
          numRatings: 24,
          recommended: false,
          photo: 'https://spoonuniversity.com/wp-content/uploads/sites/23/2015/07/clarkkerr_int-copy-2-1024x709.jpg',
          link: '/crossroads',
          foods: [
            {
              name: 'Burrito',
              imageUrl: 'https://www.simplyrecipes.com/thmb/wL--Gf181yz-4sXRmM7X24IxTn8=/2000x1333/filters:fill(auto,1)/__opt__aboutcom__coeus__resources__content_migration__simply_recipes__uploads__2018__04__Freezer-Breakfast-Burritos-LEAD-1-531741f1b8c54ad6b3b89e199f6b70b8.jpg'
            },
            {
              name: 'Pizza',
              imageUrl: 'https://www.berkeleyside.org/wp-content/uploads/2018/01/Lucias.jpg'
            },
            {
              name: 'Apple Pie',
              imageUrl: 'https://kristineskitchenblog.com/wp-content/uploads/2021/04/apple-pie-1200-square-592-2.jpg'
            }
          ],
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
            {
              uid: '21902i1a3292j12',
              first_name: 'Caleb',
              last_name: 'Kim',
              photo: 'https://media-exp1.licdn.com/dms/image/C5603AQFwp44-wj76vw/profile-displayphoto-shrink_800_800/0/1633849143227?e=1640217600&v=beta&t=S85BMzOaqFub7TaefH3-kUmQS2o5lbAFsPCedjUSKZg',
              entered: '5:47PM'
            }
          ]
        },
        {
          name: 'Foothill',
          score: 8.8,
          rating: 4,
          numRatings: 13,
          recommended: false,
          photo: 'https://foothill.edu/facilityrentals/images/facilityrentals_1300.jpg',
          link: '/crossroads',
          foods: [
            {
              name: 'Pasta',
              imageUrl: 'https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F9%2F2020%2F09%2F17%2Fcream-tomato-rigatoni-FT-RECIPE1020.jpg'
            },
            {
              name: 'Cookies',
              imageUrl: 'https://images-gmi-pmc.edge-generalmills.com/087d17eb-500e-4b26-abd1-4f9ffa96a2c6.jpg'
            },
            {
              name: 'Salad',
              imageUrl: 'https://kristineskitchenblog.com/wp-content/uploads/2020/06/italian-salad-1200-1401.jpg'
            }
          ],
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
            }
          ]
        },
        {
          name: 'Golden Bear Café',
          score: 6.8,
          rating: 4.5,
          numRatings: 76,
          recommended: false,
          photo: 'https://spoonuniversity.com/wp-content/uploads/sites/23/2016/03/DSC_0018-1024x682.jpg',
          link: '/crossroads',
          foods: [
            {
              name: 'Meatloaf',
              imageUrl: 'https://www.rachelcooks.com/wp-content/uploads/2019/12/meatloaf-web-2-of-6.jpg'
            },
            {
              name: 'Yaki Soba',
              imageUrl: 'https://www.justonecookbook.com/wp-content/uploads/2020/04/Yakisoba-5416-I-500x500.jpg'
            },
            {
              name: 'Bananas',
              imageUrl: 'https://images.squarespace-cdn.com/content/v1/5dc3865420332b6418d6690a/1603555723584-PNY06RFTM3Q7QVNPGBLN/IMG_0888.jpg'
            }
          ],
          students: [
            {
              uid: '21902i192j12',
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

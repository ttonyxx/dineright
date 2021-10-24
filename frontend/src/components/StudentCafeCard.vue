<template>
  <div>
  <v-card
    :loading="loading"
    class="mx-auto my-12"
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
      src="https://i2.wp.com/www.dailycal.org/assets/uploads/2016/11/patz_mikaelaRaphael_staff-900x580.jpg"
    ></v-img>

    <v-card-title>CROSSROADS <v-chip class="ml-2" color="green lighten-3">8.9</v-chip></v-card-title>

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
            4.5 (54)
          </div>
          <v-rating
            :value="4.5"
            color="amber"
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
                color="var(--main-yellow)">4 friends</v-chip>
            </template>

            <v-card>
              <v-card-title class="grey lighten-2" style="font-family: var(--main-font);">
                <v-chip color="var(--main-yellow)" style="font-size: 18px; margin-right: 5px;">4 friends</v-chip> at Crossroads
              </v-card-title>

              <v-card-text>
                <v-list style="overflow: hidden;">
                  <template v-for="(student, i) in students">
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
        v-model="selection"
        active-class="deep-purple accent-4 white--text"
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
          <div class="menu-item">
            Terryaki<br>
            <v-img style="display: inline-block; border-radius: 5px;" height="80px" width="80px" src="@/assets/terryaki.jpg"></v-img>
          </div>

          <div class="menu-item">
            Macaroni<br>
            <v-img style="display: inline-block; border-radius: 5px;" height="80px" width="80px" src="https://i.pinimg.com/originals/6d/f8/c6/6df8c6eae5371ebb2d583da21214b8f0.jpg"></v-img>
          </div>

          <div class="menu-item">
            Tacos<br>
            <v-img style="display: inline-block; border-radius: 5px;" height="80px" width="80px" src="https://i.pinimg.com/originals/c4/9b/1e/c49b1e57b208b5d4a0790eaeab0fc285.jpg"></v-img>
          </div>
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

export default {
  name: 'StudentCafeCard',
  components: {
      StudentListItem
  },

  created() {
    
  },

  watch: {
      
  },

  data() {
    return {
      dialog: false,
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

      ]
    }
  },

  computed: {
  },

  methods: {
    
  },

}
</script>

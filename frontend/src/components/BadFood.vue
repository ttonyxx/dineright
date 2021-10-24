<template>
  <div>
    <v-app style = "background-color : var(--main-gray); margin-left: -200px; ">
      <v-card max-width="1000" class="mx-auto">


        <v-app-bar dark color=#15284B>
          <v-toolbar-title>Worst Food Items</v-toolbar-title>

          <v-spacer></v-spacer>

        </v-app-bar>

        <v-container>
          <v-row dense>
            <v-col v-for="(item, i) in items" :key="i" cols="12">
              <v-card :color="item.color" dark>
                <div class="d-flex flex-no-wrap justify-space-between">
                  <div>
                    <v-card-title
                      class="text-h5"
                      v-text="item.menuitem"
                    ></v-card-title>

                    <v-card-subtitle v-text="item.description" style="text-align: left;"></v-card-subtitle>
                    <div style="display: flex;">
                      <v-card-subtitle v-text="item.rating" style="text-align: center; background-color: #15284B; border-radius: 20px; max-width: 75px; margin-left: 10px; font-weight: Bold;"></v-card-subtitle>
                      <v-card-subtitle v-text="item.change" style="text-align: center; background-color: #15284B; border-radius: 20px; max-width: 150px; margin-left: 10px; font-weight: Bold;"></v-card-subtitle>
                    </div>

                  </div>
                  <v-avatar class="ma-3" size="125" tile>
                    <v-img :src="item.src" style="border-radius: 20px;"></v-img>
                  </v-avatar>



                </div>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </v-card>
    </v-app>
  </div>
  
</template>

<script>

export default {
  name: 'BadFood',

  props: {
    items: { type: Object, required: true }
  },

  components: {
      
  },

  created() {
  },

  watch: {
      
  },
  


  data() {
    return {
      dialog: false,
      
    }
  },

  computed: {
  },

  methods: {
    
  },

}
</script>
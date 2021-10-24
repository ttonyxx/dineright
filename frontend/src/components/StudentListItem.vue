<template>
  <v-list-item style="width: 350px;">
    <v-list-item-avatar size="42px" style="margin-left: -15px;">
      <img
        alt="Avatar"
        :src="student.photo"
        style="background-color: #F5F5F5;"
      />
    </v-list-item-avatar>
    <v-list-item-content style="font-family: var(--main-font);">
      <v-row align="left">
        <v-col cols="auto" class="py-0 pr-0" style="margin-left: 0px;" align="left">
          <v-list-item-title style="margin-top: 15px;"><v-chip class="mr-1">{{ student.first_name }} {{ student.last_name }}</v-chip> </v-list-item-title>
          <v-card-subtitle style="margin-top: -15px; margin-left: -10px; font-size: 12px;" color="gray">
              Entered at {{ student.entered }}
            </v-card-subtitle>
        </v-col>

      </v-row>
    </v-list-item-content>

    <v-list-item-action>
      
    </v-list-item-action>
  </v-list-item>
</template>

<script>
export default {
  name: 'StudentListItem',
  props: {
    student: {type: Object, required: true},
  },
  data() {
    return {
    }
  },
  computed: {
  },
  methods: {
  },
}
</script>
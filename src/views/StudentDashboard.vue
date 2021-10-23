<template>
  <v-container class="studentdashboard">

      <StudentCafeCard></StudentCafeCard>
  
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

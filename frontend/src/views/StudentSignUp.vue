<template>
  <div style="width: 350px; margin: auto;">
    <h2>Sign Up</h2>
    <br>
    <v-text-field
      label="Name"
      filled
      v-model="name"
    ></v-text-field>
    <v-text-field
      label="Email"
      filled
      v-model="email"
    ></v-text-field>
    <v-text-field
      label="Password"
      type="password"
      v-model="password"
    ></v-text-field>
    <v-btn elevation="2" @click="signUp">Sign In</v-btn>
  </div>
</template>

<script>
import { post } from '@/utils';
export default {
  data() {
    return {
      name: '',
      email: '',
      password: ''
    }
  },
  methods: {
    signUp() {
      post('/create-account', {
        name: this.name,
        email: this.email,
        password: this.password
      }).then(res => {
        if (res.success) {
          console.log('Account Created!');
        }
      })
    }
  }
}
</script>
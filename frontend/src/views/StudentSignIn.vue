<template>
  <div style="width: 350px; margin: auto;">
    <h2>Sign In</h2>
    <br>
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
    <v-btn elevation="2" @click="signIn">Sign In</v-btn>
  </div>
</template>

<script>
import { post, state } from '@/utils';

export default {
  data() {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    signIn() {
      post('/valid-user', {
        email: this.email,
        password: this.password
      }).then(res => {
        if (res.success) {
          state.set('user', res.data);
          state.dispatch('user_set');
          this.$router.push({ path: '/' });
        } else alert('Wrong username/password combination');
      }).catch(() => {
        alert('Encountered an while trying to validate username/password combination');
      });
    }
  }
}
</script>
<template>
  <div>
    <h1>Processing your authentication...</h1>
  </div>
</template>

<script>
import axios from 'axios'; // 引入axios

export default {
  created() {
    this.handleAuthentication();
  },
  methods: {
    handleAuthentication() {
      const code = new URLSearchParams(this.$route.query).get('code');
      console.log(11111111111111)
      if (code) {
        console.log(1, code)
        axios.post(`http://localhost:8000/callback?code=${code}`,)
          .then(response => {
            console.log("response",response)
            localStorage.setItem('access_token', response.data.access_token);
            this.$router.push('/');
          })
          .catch(() => {
            this.$router.push('/login');
          });
      } else {
        this.$router.push('/login');
      }
    }
  }
}
</script>

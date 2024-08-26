<template>
  <div>
    <h1>Login</h1>
    <button @click="redirectToSSO">Login with SSO</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  methods: {
    redirectToSSO() {
      const ssoLoginUrl = "http://localhost:8000/login?redirect_uri=http://backend:8080/auth/callback";
      window.location.href = ssoLoginUrl;
    }
  }
}
</script>

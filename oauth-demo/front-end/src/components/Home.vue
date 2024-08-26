<template>
  <div>
    <h1>Home</h1>
    <p>Welcome to the Home page!</p>
    <button @click="logout">Logout</button>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      localStorage.removeItem('access_token');
      this.$router.push('/login');
    }
  }
}
</script>

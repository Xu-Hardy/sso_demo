<template>
  <div id="app">
    <!-- Main layout can go here, e.g., header, nav, main content area, footer -->
    <header>
      <h1>My App</h1>
      <!-- Navigation links or navbar component -->
    </header>

    <!-- Router View -->
    <!-- This component is where your routed components will be displayed -->
    <router-view />

    <footer>
      <p>© 2024 My Awesome Vue App</p>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App'
  // You can define global components here if needed
  // components: {
  //   Navbar,
  //   Footer
  // }
}
</script>

<style>
/* Global styles for your app */
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

header {
  background: #42b983;
  padding: 15px;
  color: white;
}

footer {
  background: #35495e;
  padding: 10px 0;
  color: white;
  position: fixed;
  bottom: 0;
  width: 100%;
}
</style>

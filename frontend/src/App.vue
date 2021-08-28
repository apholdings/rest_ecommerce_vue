<template>
  <element id="nav">
  <Navbar></Navbar>
  </element>
  <router-view/>
</template>

<script>
import Navbar from './components/Navbar.vue'

export default {
  name: 'Home',
  components: {
    Navbar
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav a {
  font-weight: Bold;
  color: #5e6a75;
}

#nav a.router-link-exact-active {
  font-weight: bold;
  color: #111827;
  --tw-border-opacity: 1;
  border-color: rgba(99, 102, 241, var(--tw-border-opacity));
}
</style>

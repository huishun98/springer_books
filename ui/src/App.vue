<template>
  <div class="app">
    <Books />
  </div>
</template>

<script>
import Books from './components/Books.vue'

export default {
  name: 'App',
  components: {
    Books
  }
}
</script>

<style>
:root {
  --default-font-size: 14px;
}
.app {
  font-size: var(--default-font-size);
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
a:hover {
    text-decoration: none;
}
</style>

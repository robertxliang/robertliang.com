<template>
  <div id="app">
    <navigation/>
    <router-view></router-view>
    <About/>
    <Contact/>
    <Footer/>
    
  </div>
</template>

<script>
import About from './components/includes/about.vue'
import Contact from './components/includes/contact.vue'
import Footer from './components/includes/footer.vue'

export default {
  name: 'App',
  components: {
    About,
    Contact,
    Footer,
  }
}
</script>

<style>
#app {
  font-family: Montserrat, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #585e64;
}
</style>

<template>
  <div id="back-ground">
    <Header />
    <Nuxt class="mainpage" />
    <Footer />
  </div>
</template>

<script>
import { Header } from '~/components/Header'
import { Footer } from '~/components/Footer'
export default {
  components: {
    Header,
    Footer,
  },
}
</script>

<style>
#back-ground {
  background-color: antiquewhite;
}
.main-color {
  background-color: #adb367;
  color: white;
}
.mainpage {
  min-height: 100vh;
}
@font-face {
  font-family: '衡山毛筆フォント行書';
  src: url('../assets/font/KouzanGyoushoOTF.otf') format('opentype');
}
.haiku-font {
  font-family: '衡山毛筆フォント行書', serif;
}
</style>

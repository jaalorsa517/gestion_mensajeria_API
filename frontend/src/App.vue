<template lang="pug">
  #app
    h1 Getión de mensajeros
    router-view
</template>

<style lang="stylus">
//Mixins


html
  margin 0
  padding 0

body
  size-box(95vh,95vh)
  margin auto
  background-color color-back
  
h1,h2, a, input, input:active, ::placeholder
  color color-fonts
  shadow-text()

a:visited
  color color-1

input
  padding 10px
  background-color color-2
  border none
  border-radius 5px
  shadow-box()

#app
  size-box(100%,100)
  font-family Avenir, Helvetica, Arial, sans-serif
  text-align center
  color color-fonts
  background-color color-back

.link
	margin-roof-floor(10px)
</style>

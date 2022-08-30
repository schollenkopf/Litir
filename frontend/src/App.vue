<template>
  <div class="frame">
      <menu-bar />
     
      <router-view class="router"/>
    </div>
</template>

<script>
import MenuBar from "./components/MenuBar.vue"
export default {
  
  components: { MenuBar }
};

</script>

<style>
.frame{
    position: absolute;
    height: 100%;
    width: 100%;
   
  }
.router{
  position: relative;
  height: 100%;
}

</style>

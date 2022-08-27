<template>
  <div class="frame">
      <menu-bar />
     
      <router-view />
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

    width: 100%;
    top: 0px;
    right: 0px;
    left: 0px;
    bottom: 0px;
  }

</style>

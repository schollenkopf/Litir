<template>
  <div class="frame">
      <menu-bar />
     
     
      <router-view class="router" v-slot="{ Component }">
        <transition name="fade">
          <component :is="Component" />
        </transition>
      </router-view>
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

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

</style>


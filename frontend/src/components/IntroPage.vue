<template>

  
  

  
    <div class="body" key="intro">
      <div class="introText" style="font-size: 45px; 
    font-weight: 550; margin-top: 50px">
        Empowering Financial Analysis
      </div>
      <div class="introText">
        Estimate a company's valuation in minutes!
      </div>
      <button class="openApplication" @click="openApplication">
        Open Application
      </button>
    </div>



</template>

<script>
import router from '@/router';

export default {
  name: 'IntroPage',

  components: {

  },

  data: () => ({
    //
  }),
  methods: {
    openApplication(){
      router.push("/login");
    }
  }
}
</script>

<style>
  
  
   .body{
    overflow-x: hidden;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
    background-color: rgb(255, 255, 255);
    align-items: center;   
    
    left: inherit;
    right: inherit;
    
    bottom: inherit;
   }
   .openApplication{
    width: 420px;
    height: 40px;
    text-align: center center;
    margin-top: 20px;
    font-family: Open Sans; 
    font-size: 18px; 
    font-weight: 300; 
    color: rgb(226, 226, 226); 
    line-height: 1.4; 
    border-radius: 5px; 
    background-color:  rgb(10, 48, 0);

   }
   .openApplication:hover{
    background-color:  rgb(38, 136, 13);
    font-size: 20px; 

    color: rgb(255, 255, 255); 
   }
   .introText{
    margin-top: 20px;
    font-family: Open Sans; 
    font-size: 24px; 
    font-weight: 300; 

   }
   .fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

</style>

<template>
<div class="frame">
  <div class="topmenu" >
      <div class="logo" style="" ></div>
        <button class="menuButton" >
          About
        </button>
        <button class="menuButton" >
          Use Cases
        </button>
  </div>
  <div class="body">
    <button class="openApplication" @click="openApplication">
      Open Application
    </button>
  </div>
</div>
</template>

<script>


export default {
  name: 'App',

  components: {

  },

  data: () => ({
    //
  }),
  methods: {
    
  }
}
</script>

<style>
  .frame{

    width: 100%;
    top: 0px;
    right: 0px;
    left: 0px;
    bottom: 0px;
  }
  .topmenu{
    margin-right: auto; 
    width: initial; 
 
    left: 0px; 
    right: 0px; 
    top: 0px;
  
    height: 50px;
    max-height: calc(100% - 0px); 
    position: fixed;

    background-color: rgb(10, 48, 0); 
    display: flex;
  flex-direction:row; 
  align-items: center;

  }
  .logo{
    width: 75px; 
    height: 28px; 
    margin-left: 10px; 
    background-repeat: no-repeat; 
    background-position: center center; 
    background-size: cover;
    background-image: url(https://d1muf25xaso8hp.cloudfront.net/https%3A%2F%2Fs3.amazonaws.com%2Fappforest_uf%2Ff1655377993027x901756943804952400%2FLitir%2520Logo.png?w=96&amp;h=&amp;auto=compress&amp;dpr=2&amp;fit=max&);
   }
   .menuButton{
    align-self: center center; 
    margin-left: 50px;
    width: 90px;
    cursor: pointer; 
    text-align: center; 
    font-family: Open Sans; 
    font-size: 18px; 
    font-weight: 300; 
    color: rgb(226, 226, 226); 
    line-height: 1.4; 
    border-radius: 5px; 
    
   }
   .menuButton:hover{
    font-size: 20px; 
    font-weight: 400; 
    color: rgb(255, 255, 255); 
   }
   .body{

    background-color: rgb(255, 255, 255);

    left: inherit;
    right: inherit;
    margin-top: 50px;
    bottom: inherit;
   }
   .openApplication{
    width: 200px;
    height: 30px;
    text-align: center center;
    margin-top: 400px; 
    font-family: Open Sans; 
    font-size: 18px; 
    font-weight: 300; 
    color: rgb(226, 226, 226); 
    line-height: 1.4; 
    border-radius: 15px; 
    background-color:  rgb(10, 48, 0);

   }

</style>

<template>
    <div class="mainBody">
        
        <SidePanel/>
        <MyProjects/>
    </div>
  
      
    


</template>
<script>
import SidePanel from "./SidePanel.vue";
import MyProjects from "./MyProjects.vue";


export default{

    components: { SidePanel, MyProjects }
}

</script>

<style>
.mainBody{
    flex-direction: row;
    display: flex;
    height: 100%;
    background-color: rgb(255, 255, 255);
    
}

</style>
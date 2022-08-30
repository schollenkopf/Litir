<template>

<div class="panel" >
    <div class="userNameBox">
        <div class="userName">
            Paul_becker
        </div>
    </div>
    <div class="panelItemBox">
        <div class="panelItemIcon" style="background-image: url(&quot;https://d1muf25xaso8hp.cloudfront.net/https%3A%2F%2Fs3.amazonaws.com%2Fappforest_uf%2Ff1649879449985x274426613414709100%2Fbaseline_space_dashboard_black_24dp.png?w=24&amp;h=&amp;auto=compress&amp;dpr=2&amp;fit=max&quot;)"/>
        <button class="panelButton">
            Dashboard
        </button>
    </div>
    <div class="panelItemBox" style="background-color: rgb(10, 48, 0);" >
        <div class="panelItemIcon" style="background-image: url(&quot;https://d1muf25xaso8hp.cloudfront.net/https%3A%2F%2Fs3.amazonaws.com%2Fappforest_uf%2Ff1650136439265x909321798474690400%2Fround_business_white_24dp.png?w=24&amp;h=&amp;auto=compress&amp;dpr=2&amp;fit=max&quot;)" />

        <button class="panelButton" style="color:rgb(255, 255, 255); ">
             Projects
        </button>
    </div>
    <div class="panelItemBox">
        <div class="panelItemIcon" style="background-image: url(&quot;https://d1muf25xaso8hp.cloudfront.net/https%3A%2F%2Fs3.amazonaws.com%2Fappforest_uf%2Ff1653736303211x738379671939353900%2Fbaseline_analytics_black_24dp.png?w=24&amp;h=&amp;auto=compress&amp;dpr=2&amp;fit=max&quot;);"/>
        <button class="panelButton">
            Valuation Metrics
        </button>
    </div>
    <div class="panelItemBox">
        <div class="panelItemIcon" style="background-image: url(&quot;https://dd7tel2830j4w.cloudfront.net/f1653736583668x500593477936313900/group_work_black_24dp.svg&quot;);"/>
        <button class="panelButton">
            Team Workspace
        </button>
    </div>
    <div class="panelItemBox">
        <div class="panelItemIcon" style="background-image: url(&quot;https://d1muf25xaso8hp.cloudfront.net/https%3A%2F%2Fs3.amazonaws.com%2Fappforest_uf%2Ff1654110968244x954516816422324100%2Fbaseline_compost_black_24dp.png?w=24&amp;h=&amp;auto=compress&amp;dpr=2&amp;fit=max&quot;);"/>
        <button class="panelButton">
            ESG Metrics
        </button>
    </div>
</div>

</template>

<style>
.panel{
    
  
    justify-content: flex-start;    height: initial; width: 200px; position: relative;  background-color: rgb(214, 214, 214); border-radius: 0px;
}
.userNameBox{
    
     align-self: flex-start; min-width: 126px; order: 1; min-height: 0px; max-height: 60px; flex-grow: 1; width: calc(100% - 10px); margin: 0px 5px 0px; justify-content: flex-start; overflow: visible; border-radius: 0px; border-bottom: 1px solid rgb(255, 255, 255); cursor: pointer;
}
.userName{
    align-content: center;
    margin-left: 5px; margin-bottom: 8px;
    align-self: flex-start; min-width: 0px; max-width: 160px; order: 1; min-height: 0px; max-height: 50px; width: 0px; flex-grow: 1; height: max-content;  white-space: pre-wrap; overflow: visible;  font-family: Open Sans; font-size: 18px; font-weight: bold; color: rgb(0, 0, 0); line-height: 1.4; border-radius: 0px;
}
.panelItemBox{

    display: flex;
  flex-direction:row; 
    padding: 5px;
    align-self: center; min-width: 112px; order: 4; min-height: 30px; height: max-content; width: calc(100% - 0px); margin: 10px 0px 0px; overflow: visible; border-radius: 0px; 
}
.panelItemBox:hover{
    background-color: rgb(236, 235, 235); 
}
.panelItemIcon{
    align-self: center;

    margin-left: 10px;
    min-width: 20px; max-width: 20px; order: 1; min-height: 20px; max-height: 20px; width: 20px; flex-grow: 1; height: 20px; border-radius: 0px; background-color: rgba(255, 255, 255, 0); background-repeat: no-repeat; background-position: center center; background-size: cover; 
}
.panelButton{
    align-self: center;
    margin-left: 5px;
    min-width: 0px; order: 2; min-height: 0px;  flex-grow: 1; height: max-content; padding: 0px; cursor: inherit; text-align: left; user-select: none; font-family: Open Sans; font-size: 17px; font-weight: bold; color: rgb(0, 0, 0); line-height: 1.4; border-radius: 3px; 
}


</style>


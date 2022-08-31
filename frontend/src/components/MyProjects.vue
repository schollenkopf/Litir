<template>
    <Transition name="slide-fade" mode="out-in">
        
        <table v-if="showTable">
            <thead >
                <tr>
                    <th class="headeritem" v-for="name in fieldnames" :key="name">{{name}}</th>
                    
                </tr>
            </thead>
            <tbody>
                <tr @click="clickedRow" class="datarow" v-for="project in projects" :key="project">
                    <td v-for="field in project" :key="field">{{field}}</td>
                </tr>
            </tbody>
        </table>
    </Transition>
    <Transition name="slide-fade" mode="out-in">

        <div class="details" v-if="!showTable"/>
    </Transition>


        
</template>
<script>
export default{
    data(){
        return {
            showTable: true,
            fieldnames: ["Project name","Company","Stage","Country","Creation Date","Industry"],
            projects: [["test","IKEA Aktiebolag","Screening / incoming","Sweden(SEK)","Aug 23, 2022","n/a"],["test","IKEA Aktiebolag","Screening / incoming","Sweden(SEK)","Aug 23, 2022","n/a"]]
        }
    },
    methods: {
        clickedRow(){
            this.showTable = false
        }
    },
    
}

</script>

<style>
.details {
    width: 100%;
    height: 100%;
    background-color: blue;
}
table {
    border-collapse: collapse;
    margin-right: 10px;
    margin-left: 10px;
    margin-top: 20px;
    height: max-content;
    width: 100%;
}
.headeritem{
    text-align: start;
    
    
}

tr { 
  border: solid;
  border-width: 0px 0px 1px;
  line-height: 50px;
}
tr:hover {
    background-color: rgb(10, 48, 0);
    color: white
}
.slide-fade-enter-active {
    transition: all 0.3s ease-out;
  }
  
  .slide-fade-leave-active {
    transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
  }
  
  .slide-fade-enter-from,
  .slide-fade-leave-to {
    transform: translateX(20px);
    opacity: 0;
  }
</style>
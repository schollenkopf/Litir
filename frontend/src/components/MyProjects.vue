<template>
    <Transition name="project-table" mode="out-in">
        
        <table v-if="showTable">
            <thead >
                <tr>
                    <th class="headeritem" v-for="name in fieldnames" :key="name">{{name}}</th>
                    
                </tr>
            </thead>
            <tbody>
                <tr @click="switchView" class="datarow" v-for="project in projects" :key="project">
                    <td v-for="field in project" :key="field">{{field}}</td>
                </tr>
            </tbody>
        </table>
  

        <div class="details" v-else-if="!showTable">
            <v-btn class="back"
            @click.stop="switchView"
            icon
            
          >
            <v-icon>mdi-arrow-left</v-icon>
          </v-btn>
          <div class="detailsHeader">
            <div class="detailsHeaderFirstRow">
                <div class="titleCompany">
                    {{this.projects[0][1]}}
                </div>
                <button class="detailsExpandButton">
                    <v-icon>mdi-arrow-up</v-icon>
                </button>
            </div>

          </div>
        </div>
    </Transition>


        
</template>
<script>
export default{
    data(){
        return {
            
            showTable: false,
            fieldnames: ["Project name","Company","Stage","Country","Creation Date","Industry"],
            projects: [["test","IKEA Aktiebolag","Screening / incoming","Sweden(SEK)","Aug 23, 2022","n/a"],["test","IKEA Aktiebolag","Screening / incoming","Sweden(SEK)","Aug 23, 2022","n/a"]]
        }
    },
    methods: {
        switchView(){
            this.showTable = !this.showTable
        }
    },
    
}

</script>

<style>
.detailsExpandButton{
    color: white;
    align-self: center;
    margin-left: 10px;

}
.titleCompany{
    font-size: 22px;
    color: white;
}

.detailsHeaderFirstRow{
    flex-direction: row;
    align-items: center;
    
    display: flex;

}
.detailsHeader{
    min-height: 100px;
    padding: 10px;
    margin-left: 20px;
    margin-right: 20px;
    margin-top: 10px;
    background-color: rgb(10, 48, 0);
    border-radius: 5px;
}

.back{
    height: 20px;
    margin-left: 20px;
    margin-top: 10px;
    
}
.details {
    width: 100%;
    height: 100%;
  
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
.project-table-enter-active {
    transition: all 0.3s ease-out;
  }
  
  .project-table-leave-active {
    transition: all 0.3s cubic-bezier(1, 0.5, 0.8, 1);
  }
  
  .project-table-enter-from{
    transform: translateY(100px);
  }
  .project-table-leave-to {
    opacity: 0;
    
  }


</style>
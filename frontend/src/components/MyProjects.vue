<template>
    <table >
    <thead >
        <tr>
            <th class="headeritem" v-for="name in fieldnames" :key="name">{{name}}</th>
            
        </tr>
        </thead>
        <tbody>
        <tr class="datarow" v-for="project in projects" :key="project">
      <td v-for="field in project" :key="field">{{field}}</td>
    </tr>
        </tbody>
    </table>
</template>
<script>
export default{
    data(){
        return {
            fieldnames: ["Project name","Company","Stage","Country","Creation Date","Industry"],
            projects: [["test","IKEA Aktiebolag","Screening / incoming","Sweden(SEK)","Aug 23, 2022","n/a"],["test","IKEA Aktiebolag","Screening / incoming","Sweden(SEK)","Aug 23, 2022","n/a"]]
        }
    },
    
}

</script>

<style>
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
  border-width: 1px 0;
}
tr:hover {
    background-color: green;
}

</style>
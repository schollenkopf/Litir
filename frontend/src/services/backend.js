export default class Backend{

    constructor(){
        this.url = "http://127.0.0.1:5000"
    }

    getUrlData(){
        return this.url + "/import_raw_data"
    }

    getGraph(){
        return this.url + "/get_graph"
    }

    filter(){
        return this.url + "/filter"
    }

}
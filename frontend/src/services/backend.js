export default class Backend{

    constructor(){
        this.url = "http://127.0.0.1:5000"
    }

    login(){
        return this.url + "/login"
    }

    postNewUser(){
        return this.url + "/post_new_user"
    }


}
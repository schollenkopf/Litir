<template>
    <div>
        <h1>REGISTER </h1>
        <form v-on:submit.prevent="submitForm">
            <div> 
                <input type="text" id="username" name="username" placeholder="Username" required 
                    v-model="form.username" />
            </div>
            <div> 
                <input type="email" id="email" name="email" placeholder="Email" required 
                    v-model="form.email" />
            </div>
            <div>
                <input type="password" id="password" name="password" placeholder="Password" required
                    v-model="form.password" />
            </div>
            <div>
                <input type="password" id="repeatPassword" name="repeatPassword" placeholder="Repeat Password" required
                    v-model="form.repeatPassword" />
            </div>
            <div>
                <button type="submit">Register</button>
            </div>
        </form>
        <button @click="goToLoginPage"> Already registered? Login here </button>
    </div>
</template>

<script>
import router from '@/router';

export default {
    data() {
        return {
            form: {
                username: "",
                email: "",
                password: "",
                repeatPassword: "",
            }
        }
    },
    methods: {
        submitForm() {
            this.axios.post(this.$backend.postNewUser(), this.form)
                .then((response) => {
                    var a = response
                    console.log(a)
                    console.log(response.status)
                    if(response.status == 277){
                        console.log(response.data)
                    }
                    else{
                        console.log("NEW USER CREATED");
                    }
                })
        },
        goToLoginPage(){
            router.push("/login");
        },
    }
}
</script>

<style>

</style>
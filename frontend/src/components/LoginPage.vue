<template>
    <div>
        <h1>LOGIN </h1>
        <form v-on:submit.prevent="submitForm">
            <div> 
                <input type="email" id="email" name="email" placeholder="Email" required 
                    v-model="form.email" />
            </div>
            <div>
                <input type="password" id="password" name="password" placeholder="Password" required
                    v-model="form.password" />
            </div>
            <div>
                <button type="submit">Login</button>
            </div>
        </form>
        <button @click="goToRegiserPage">
        Register
      </button>
    </div>
</template>

<script>
import router from '@/router';

export default {
    data() {
        return {
            form: {
                email: "",
                password: "",
            }
        }
    },
    methods: {
        submitForm() {
            try {
                this.axios.post(this.$backend.login(), this.form)
                    .then((response) => {
                        var a = response
                        console.log(a)
                        console.log(response.status)
                        if(response.status == 277){
                            console.log(response.data)
                        }
                        else if(response.status == 266){
                            console.log(response.data)
                        }
                        else{
                            router.push("/application");
                        }
                    })
            }
            catch (e) {
                console.log(e);
            }
        },
        goToRegiserPage(){
            router.push("/register");
        }
    }
}
</script>

<style>

</style>
<template>
    <div class="login-container">
        <h1>Bienvenido</h1>
        <form @submit.prevent="login" class="login-form">
            <label for="email">Email:</label>
            <input type="text" id="email" v-model="email" required>
            <label for="password">Password:</label>
            <input type="password" id="password" v-model="password" required>
            <button type="submit">Iniciar sesión</button>
            <p>No tienes cuenta? <RouterLink to="/register-profesional">Registrate</RouterLink></p>
        </form>
    </div>
</template>


<script>
import axios from 'axios';
    export default {
        data() {
            return {
                email: '',
                password: ''
            }
        },
        methods: {
            login(){
                axios.post('login', {
                    email: this.email,
                    password: this.password
                }).then(response => {
                    console.log(response)
                    this.$router.push({name: 'home'})
                }).catch(error => {
                    console.log(error)
                })
            }
            
        }
    }
</script>

<style scoped>
.login-container {
    width: 90%;
    max-width: 350px;
    margin: 0 auto;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 50vh; 
}

h1 {
    font-size: 1.6em;
    margin-bottom: 20px;
    color: #404040;
}

.login-form label {
    display: block;
    margin-bottom: 5px;
    font-size: 1em;
}

.login-form input {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 4px;
    border: 1px solid #ccc;
    font-size: 0.9em;
}

.login-form button {
    width: 100%;
    padding: 10px;
    background-color: #52A6FE;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1em;
}

.login-form button:hover {
    background-color: #248cfb;
}

.login-form p {
    margin-top: 20px;
    font-size: 0.9em;
}

@media (min-width: 600px) {
    .login-container {
        width: 50%;
    }

    h1 {
        font-size: 1.8em;
    }

    .login-form label {
        font-size: 1.1em;
    }

    .login-form input {
        font-size: 1em;
    }

    .login-form button {
        font-size: 1.1em;
    }

    .login-form p {
        font-size: 1em;
    }
}
</style>
<template>
    <div class="register-container">
        <form @submit.prevent="register" class="register-form">
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" v-model="nombre" required>
            <label for="apellido">Apellido:</label>
            <input type="text" id="apellido" v-model="apellido" required>
            <label for="comuna">Comuna:</label>
            <input type="text" id="comuna" v-model="comuna" required>
            <label for="Direccion">Direccion:</label>
            <input type="text" id="direccion" v-model="direccion" required>
            <label for="email">Email:</label>
            <input type="email" id="email" v-model="email" required>
            <label for="password">Password:</label>
            <input type="password" id="passwordr" v-model="password" required>
            <label for="confirmPassword">Confirm Password:</label>
            <input type="password" id="confirmPassword" v-model="confirmPassword" required>
            <div v-if="errorMessage" class="error-message">{{ errorMessage }}</div>
            <button type="submit">Registrarse</button>
            <p class="text-center mt-4">Ya tienes una cuenta? <RouterLink to="/login-paciente">Inicia sesión</RouterLink></p>
        </form>
    </div>
</template>


<script>
import axios from 'axios';
    export default {
        data() {
            return {
                nombre: '',
                apellido: '',
                comuna: '',
                direccion: '',
                email: '',
                password: '',
                role: 'paciente',
                errorMessage: '',
                confirmPassword: ''
            }
        },
        methods: {
    register() {
        if(this.password !== this.confirmPassword){
                    alert('Las contraseñas no coinciden');
                    return;
                }
                axios.post('/register', {
                    name: this.nombre,
                    last_name: this.apellido,
                    comuna: this.comuna,
                    direccion: this.direccion,
                    email: this.email,
                    password: this.password,
                    role: this.role,
                })
                .then(response => {
                    return new Promise((resolve, reject) => {
                        localStorage.setItem('flashMessage', 'Tu cuenta ha sido creada correctamente. Por favor inicia sesión.');
                        resolve();
                    });
                })
                .then(() => {
                    this.$router.push('/login-paciente');
                })
                .catch(error => {
                    if (error.response.status === 400) {
                        this.errorMessage = error.response.data.message;
                        console.log(error.response.data.message);
                        // Aquí puedes mostrar un mensaje de error al usuario
                    } else {
                        console.log('Ocurrió un error inesperado');
                    }
                });
    }
}
    }
</script>

<style scoped>
.register-container {
    max-width: 300px;
    width: 100%;
    margin: 0 auto;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    border-radius: 8px;
}
.error-message {
    color: red;
}

.register-form label {
    display: block;
    margin-bottom: 5px;
}

.register-form input {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 4px;
    border: 1px solid #ccc;
}

.register-form button {
    width: 100%;
    padding: 10px;
    background-color: #52A6FE;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.register-form button:hover {
    background-color: #248cfb;
}
</style>
<script setup>
import Login from '../components/LoginProfesional.vue';
import { useRouter } from 'vue-router';
</script>

<template>
  <main>
    <router-link to="/" class="back-button">Volver</router-link>
    <h1>Inicia sesión - Profesional</h1>
    <Login/>
  </main>
</template>

<style scoped>
main {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    padding: 20px;
    box-sizing: border-box;
    position: relative;
}

.back-button {
    position: absolute;
    top: 20px;
    left: 20px;
    background-color: #404040;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    text-decoration: none;
}

h1 {
    font-size: 1.8em;
    margin-bottom: 20px;
    text-align: center;
    color: #404040;
}

@media (min-width: 600px) {
    h1 {
        font-size: 2em;
    }
}
</style>
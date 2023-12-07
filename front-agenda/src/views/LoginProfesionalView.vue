<script setup>
import Login from '../components/LoginProfesional.vue';
</script>


<template>
  
  <main>
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
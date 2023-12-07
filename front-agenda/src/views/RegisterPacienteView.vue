<script setup>
import RegisterPaciente from '../components/RegisterPaciente.vue';
</script>

<template>
  
  <div class="center-container">
      <h1>Registro - Paciente</h1>
      <RegisterPaciente class="login-form"/>
  </div>
</template>

<style scoped>
.center-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

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
}

h1 {
    text-align: center;
    font-size: 1.6em;
    margin-bottom: 20px;
    color: #404040;
}

.login-form {
    width: 100%;
}

@media (min-width: 600px) {
    .login-container {
        width: 50%;
    }

    h1 {
        font-size: 1.8em;
    }
}
</style>

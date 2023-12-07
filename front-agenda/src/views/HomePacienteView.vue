<script setup>
import axios from 'axios';
import { useRouter } from 'vue-router';
import Disponibilidades from '../components/Disponibilidades.vue';

const router = useRouter();

const logout = async () => {
    try {
        await axios.get('/logout');
        router.push('/login-paciente');
    } catch (error) {
        console.error(error);
    }
};

</script>


<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title>Situ</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn @click="logout">Cerrar sesión</v-btn>
    </v-app-bar>
    <v-main>
      <h1>Disponibilidad de los profesionales</h1>
      <p>Busca la especialidad que necesites y agenda una cita</p>
      <Disponibilidades/>
    </v-main>
  </v-app>
</template>

<style scoped>
.v-app-bar {
    font-size: 1.2em;
    background-color: black !important;
}
h1 {
    text-align: start;
    font-size: 1.6em;
    margin-bottom: 20px;
    color: #404040;
}
.v-main {
    padding: 20px;
    margin-top: 64px;
}

.v-toolbar-title {
    font-size: 1.4em;
    color: white;
}

.v-btn {
    font-size: 12px;
    color: white;
}

.v-main {
    padding: 20px;
}

.v-main h1 {
    font-size: 1.6em;
    margin-bottom: 20px;
    text-align: center;
}

@media (max-width: 600px) {
    .v-app-bar {
        font-size: 1em;
    }

    .v-toolbar-title {
        font-size: 1.2em;
    }

    .v-btn {
        font-size: 0.8em;
        color: white;
    }

    .v-main h1 {
        font-size: 1.4em;
    }
}
</style>
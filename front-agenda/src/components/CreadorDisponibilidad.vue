<template>
    <div class="disponibilidad-creador-container">
        <h4>Añade nuevos horarios disponibles a tu agenda</h4>
        <form @submit.prevent="submitForm" class="disponibilidad-creador-form">
            <label for="fecha">Fecha:</label>
            <input type="date" id="fecha" v-model="fecha" required>
            <label for="hora">Hora inicio:</label>
            <input type="time" id="hora_inicio" v-model="hora_inicio" required>
            <label for="hora">Hora fin:</label>
            <input type="time" id="hora_fin" v-model="hora_fin" required>
            <button type="submit">Crear</button>
        </form>
    </div>
</template>

<!-- <template>
    <v-container class="disponibilidad-creador-container">
      <v-card class="pa-4">
        <v-card-title>Crea una Disponibilidad</v-card-title>
        <v-card-text>
          <v-form @submit.prevent="submitForm">
            <v-row>
              <v-col cols="6">
                <v-date-picker v-model="fecha" label="Fecha" required></v-date-picker>
              </v-col>
              <v-col cols="6">
                <label for="hora">Hora inicio:</label>
                <input type="time" id="hora_inicio" v-model="hora_inicio" required>
                <label for="hora">Hora fin:</label>
                <input type="time" id="hora_fin" v-model="hora_fin" required>
              </v-col>
            </v-row>
            <v-btn type="submit" color="primary">Crear</v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-container>
  </template> -->

<script>
import axios from 'axios';
import { useStore } from '@/stores/store.js';

export default {
    data() {
        return {
      fecha: new Date(),
      hora_inicio: '',
      hora_fin: '',
      estado: ''
    }
    },
    methods: {
        submitForm() {
  const store = useStore();
  axios.post('/disponibilidad', {
    fecha: this.fecha,
    hora_inicio: this.hora_inicio,
    hora_fin: this.hora_fin,
  })
  .then(response => {
    console.log(response);
    // Agrega la nueva disponibilidad a la tienda
    store.addDisponibilidad(response.data);
    store.fetchDisponibilidades();
  })
  .catch(error => {
    console.log(error);
  });
}
    }
}
</script>

<style scoped>
.disponibilidad-creador-container {
    max-width: 600px; /* Aumenta el ancho máximo según sea necesario */
    margin: 0 auto;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    border-radius: 8px;
}

.disponibilidad-creador-form label {
    display: block;
    margin-bottom: 5px;
}

.disponibilidad-creador-form input {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 4px;
    border: 1px solid #ccc;
}

.disponibilidad-creador-form button {
    width: 100%;
    padding: 10px;
    background-color: #52A6FE;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1em;
}

h4 {
    font-size: 16px;
    margin-bottom: 20px;
    
    color: #404040;
}
/* Agrega margen a los elementos de formulario para darles más espacio */
.v-form > * {
    margin-bottom: 20px;
}

.disponibilidad-creador-form button:hover {
    background-color: #248cfb;
}
</style>
<template>
    <div class="disponibilidad-creador-container">
        <h4>Añade nuevos horarios disponibles a tu agenda</h4>
        <p>Selecciona una fecha, hora de inicio y hora de fin donde podrías atender a un paciente</p>
        <form @submit.prevent="submitForm" class="disponibilidad-creador-form mt-5">
            <label for="fecha">Fecha:</label>
            <input type="date" id="fecha" v-model="fecha" required>
            <label for="hora">Hora inicio:</label>
            <input type="time" id="hora_inicio" v-model="hora_inicio" required>
            <label for="hora">Hora fin:</label>
            <input type="time" id="hora_fin" v-model="hora_fin" required>
            <button type="submit">Crear</button>
        </form>
    </div>
    <div class="container">
        <transition name="fade">
            <div v-if="flashVisible" class="flash-message">{{ flashMessage }}</div>
        </transition>
    </div>
</template>



<script>
import axios from 'axios';
import { useStore } from '@/stores/store.js';

export default {
    data() {
        return {
      fecha: new Date(),
      hora_inicio: '',
      hora_fin: '',
      estado: '',
      flashMessage: null,
      flashVisible: false
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

    // Muestra el mensaje flash
    this.flashMessage = 'La disponibilidad ha sido creada correctamente.';
    this.flashVisible = true;
    setTimeout(() => {
        this.flashVisible = false;
    }, 5000); // 
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
.container {
    display: flex;
    justify-content: center;
}

.flash-message {
    padding: 5px 10px;
    margin: 10px auto;
    border: 1px solid #007BFF;
    background-color: #D1E7FE;
    color: #007BFF;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    display: inline-flex;
    align-items: center;
    font-size: 1em;
    font-weight: bold;
}

.flash-message:before {
    content: '✔';
    margin-right: 5px;
    font-size: 1.2em;
}
</style>
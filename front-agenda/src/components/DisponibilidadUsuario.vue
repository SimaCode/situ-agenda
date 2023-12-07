<template>
    <div class="disponibilidad-container">
        <h4>Revisa tus horarios y observa la información de tus citas agendadas</h4>
       <div class="table-container">
        <table class="disponibilidad-table">
            <thead>
                <tr>
                    <th>Fecha</th>
                    <th>Hora inicio</th>
                    <th>Hora fin</th>
                    <th>Estado</th>
                    <th>Acción</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="disponibilidad in disponibilidades" :key="disponibilidad.id">
     
                    <td>{{ disponibilidad.fecha }}</td>
                    <td>{{ disponibilidad.hora_inicio }}</td>
                    <td>{{ disponibilidad.hora_fin }}</td>
                    <td>{{ disponibilidad.estado }}</td>
                    <td>
                        <button v-if="disponibilidad.estado !== 'ocupado'" @click="eliminarDisponibilidad(disponibilidad.id)" class="eliminar-btn">Eliminar</button>
                        <button v-else @click="verInfo(disponibilidad)" class="info-btn">Ver info</button>
                    </td>
                </tr>
                <!-- Ventana Modal -->
                <div v-if="modalVisible" class="modal">
                    <div class="modal-content">
                        <span @click="modalVisible = false" class="close">&times;</span>
                        <h2>Información del Paciente</h2>
                        <p>Nombre: {{ modalInfo.name }}</p>
                        <p>Apellido: {{ modalInfo.last_name }}</p>
                        <p>Email: {{ modalInfo.email }}</p>
                        <p>Comuna: {{ modalInfo.comuna }}</p>
                        <p>Dirección: {{ modalInfo.direccion }}</p>
                    </div>
                </div>
            </tbody>
        </table>
       </div>
    </div>
</template>

<script>
import axios from 'axios';
import { useStore } from '@/stores/store.js';
export default {
    data() {
        return {
            modalVisible: false,
            modalInfo: {}
        }
    },
    computed: {
        disponibilidades() {
            const store = useStore();
            return store.disponibilidades;
        }
    },
    created() {
        const store = useStore();
        store.fetchDisponibilidades();
    },
    methods: {
    eliminarDisponibilidad(id) {
        const store = useStore();
        store.deleteDisponibilidad(id);
    },
    async verInfo(disponibilidad) {
        try {
        const response = await axios.get('cita/' + disponibilidad.id);
        this.modalInfo = response.data.paciente;
        this.modalVisible = true;
        } catch (error) {
        console.log(error);
        }
    },
}
}
</script>


<style scoped>
.disponibilidad-container {
    width: 90%;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    border-radius: 8px;
}

h4 {
    font-size: 16px;
    margin-bottom: 20px;
    color: #404040;
}

.disponibilidad-table {
    width: 100%;
    border-collapse: collapse;
}

.disponibilidad-table th, .disponibilidad-table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

.disponibilidad-table tr:nth-child(even) {
    background-color: #f2f2f2;
}

.disponibilidad-table th {
    padding-top: 12px;
    padding-bottom: 12px;
    background-color: #52A6FE;
    color: white;
}

.eliminar-btn, .info-btn {
    color: white;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
    font-size: 0.9em;
}

.eliminar-btn {
    background-color: #FE5454;
}

.eliminar-btn:hover {
    background-color: darkred;
}

.info-btn {
    background-color: #52A6FE;
}

.info-btn:hover {
    background-color: #248cfb;
}

.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0,0,0,0.4);
}

.modal-content {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}

.close {
  color: #aaaaaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}

.table-container {
    overflow-x: auto;
}

@media (max-width: 600px) {
    .disponibilidad-container {
        width: 100%;
        padding: 10px;
    }

    h1 {
        font-size: 1.2em;
    }

    .disponibilidad-table th, .disponibilidad-table td {
        padding: 4px;
    }

    .eliminar-btn, .info-btn {
        font-size: 0.8em;
        padding: 3px 6px;
    }

    .modal-content {
        width: 90%;
    }
}
</style>
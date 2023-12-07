<template>
  <div class="appointments-container">
    <!-- Input de Filtro -->
    <div class="filter-input">
      <input v-model="filter" placeholder="Escribe el nombre de la especialidad que necesitas" @input="filterDisponibilidades" />
    </div>

    <!-- Tabla de Disponibilidades -->
    <div class="table-container">
      <table class="appointments-table">
        <thead>
          <tr>
            <th>Profesional</th>
            <th>Especialidad</th>
            <th>Fecha</th>
            <th>Hora inicio</th>
            <th>Hora fin</th>
            <th>Estado</th>
            <th>Acción</th>
          </tr>
        </thead>
        <tbody>
          <!-- Filas de la Tabla -->
          <tr v-for="disponibilidad in filteredDisponibilidades" :key="disponibilidad.id">
            <td>{{ disponibilidad.nombre_usuario }}</td>
            <td>{{ disponibilidad.especialidad }}</td>
            <td>{{ disponibilidad.fecha }}</td>
            <td>{{ disponibilidad.hora_inicio }}</td>
            <td>{{ disponibilidad.hora_fin }}</td>
            <td>{{ disponibilidad.estado }}</td>
            <td>
              <button v-if="disponibilidad.estado !== 'ocupado'" @click="agendarCita(disponibilidad.id, disponibilidad.id_profesional)" class="action-btn">Agendar cita</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      disponibilidades: [],
      filter: '',
      filteredDisponibilidades: [],
    };
  },
  async created() {
    const response = await axios.get('/disponibilidad');
    this.disponibilidades = response.data.disponibilidades;
    this.filteredDisponibilidades = this.disponibilidades;
    this.filterDisponibilidades(); 
  },
  methods: {
    filterDisponibilidades() {
      this.filteredDisponibilidades = this.disponibilidades.filter((disponibilidad) =>
        disponibilidad.especialidad.toLowerCase().includes(this.filter.toLowerCase()) && disponibilidad.estado === 'disponible'
      );
    },
    async agendarCita(idDisponibilidad, idProfesional) {
      if (confirm('¿Estás seguro de que quieres agendar esta cita?')) {
        try {
          await axios.post('/cita', {
            id_profesional: idProfesional,
            id_disponibilidad: idDisponibilidad,
          });
          const disponibilidadesResponse = await axios.get('/disponibilidad');
          this.disponibilidades = disponibilidadesResponse.data.disponibilidades;
          this.filteredDisponibilidades = this.disponibilidades;
        } catch (error) {
          console.log(error);
        }
      }
    },
  },
};
</script>

<style scoped>
.appointments-container {
  max-width: 100%;
  margin: auto;
  padding: 1rem;
}

.filter-input {
  margin-bottom: 1rem;
}

.filter-input input {
  width: 100%;
  max-width: 500px;
}

.table-container {
  overflow-x: auto;
}

.appointments-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1rem;
}

.appointments-table th,
.appointments-table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

.appointments-table th {
  background-color: #f2f2f2;
}

.action-btn {
  background-color: #52A6FE;
  color: white;
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.action-btn:hover {
  background-color: #298cf6;
}

/* Media Query para hacerlo responsive */
@media (max-width: 600px) {
  .appointments-table th,
  .appointments-table td {
    font-size: 12px;
  }
}
</style>

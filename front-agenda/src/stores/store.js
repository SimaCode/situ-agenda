import { defineStore } from 'pinia';
import axios from 'axios';

export const useStore = defineStore({
  id: 'disponibilidades',
  state: () => ({
    disponibilidades: []
  }),
  actions: {
    fetchDisponibilidades() {
      axios.get('/disponibilidad/usuario')
        .then(response => {
          this.disponibilidades = response.data.disponibilidades;
        })
        .catch(error => {
          console.log(error);
        });
    },
    addDisponibilidad(disponibilidad) {
      this.disponibilidades.push(disponibilidad);
    },
    deleteDisponibilidad(id) {
      axios.delete(`/disponibilidad/${id}`)
        .then(response => {
          this.disponibilidades = this.disponibilidades.filter(disponibilidad => disponibilidad.id !== id);
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
});
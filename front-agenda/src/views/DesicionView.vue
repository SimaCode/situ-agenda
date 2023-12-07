<template>
  <v-container class="fill-height" fluid>
    <v-row class="fill-height" align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-sheet class="pa-4" elevation="2">
          <v-row align="center" justify="center">
            <v-col class="text-center" cols="12">
              <h1 class="display-2">Agenda Situ</h1>
              <p class="subtitle-1">Bienvenido</p>
              <p class="subtitle-2 mt-5">Selecciona el tipo de usuario y comienza a gestionar tus Citas</p>
            </v-col>
          </v-row>
          <v-row align="center" justify="center">
            <v-col cols="12" sm="6"> <!-- Cambiado a 12 columnas en pantallas pequeñas -->
              <v-btn block color="primary" @click="goToProfessionalLogin">Profesional</v-btn>
            </v-col>
            <v-col cols="12" sm="6"> <!-- Cambiado a 12 columnas en pantallas pequeñas -->
              <v-btn block color="secondary" @click="goToPatientLogin">Paciente</v-btn>
            </v-col>
          </v-row>
        </v-sheet>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  methods: {
    goToProfessionalLogin() {
      this.$router.push('/login-profesional');
    },
    goToPatientLogin() {
      this.$router.push('/login-paciente');
    },
  },
};
</script>

<style scoped>
.fill-height {
  height: 100vh;
}
h1{
  font-weight: 700;
  color: #404040;
  font-size: 3rem;
  margin-bottom: 1rem;

}

.display-2 {
  font-size: 2.5rem;
  font-weight: bold;
}

.subtitle-1 {
  font-size: 1.25rem;
  margin-top: 1rem;
}
</style>
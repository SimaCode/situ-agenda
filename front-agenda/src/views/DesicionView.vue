<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-sheet class="pa-4" elevation="2">
          <v-row>
            <v-col cols="12" sm="6"> <!-- Cambiado a 12 columnas en pantallas pequeñas -->
              <v-btn block color="primary" @click="goToProfessionalLogin">Login Profesional</v-btn>
            </v-col>
            <v-col cols="12" sm="6"> <!-- Cambiado a 12 columnas en pantallas pequeñas -->
              <v-btn block color="secondary" @click="goToPatientLogin">Login Paciente</v-btn>
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
</style>
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginProfesionalView from '../views/LoginProfesionalView.vue'
import RegisterProfesionalView from '../views/RegisterProfesionalView.vue'
import DesicionView from '../views/DesicionView.vue'
import LoginPacienteView from '../views/LoginPacienteView.vue'
import HomePacienteView from '../views/HomePacienteView.vue'
import RegisterPacienteView from '../views/RegisterPacienteView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'desicion',
      component: DesicionView
    },
    {
      path: '/login-profesional',
      name: 'login-profesional',
      component: LoginProfesionalView
    },
    {
      path: '/register-profesional',
      name: 'register-profesional',
      component: RegisterProfesionalView
    },
    {
      path: '/login-paciente',
      name: 'login-paciente',
      component: LoginPacienteView
    },
    {
      path: '/register-paciente',
      name: 'register-paciente',
      component: RegisterPacienteView
    },
    
    {
      path: '/home',
      name: 'home',
      component: HomeView
    },
    {
      path: '/paciente-home',
      name: 'paciente-home',
      component: HomePacienteView
    },
  ]
})

export default router

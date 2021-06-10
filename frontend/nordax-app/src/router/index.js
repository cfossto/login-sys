import { createRouter, createWebHistory } from 'vue-router'
import Landingpage from '../views/Landingpage.vue'

const routes = [
  {
    path: '/',
    name: 'Ladningpage',
    component: Landingpage
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

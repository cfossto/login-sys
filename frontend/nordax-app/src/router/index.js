import { createRouter, createWebHistory } from 'vue-router'
import Landingpage from '../views/Landingpage.vue'
import Inside from '../views/Inside.vue'
import editUser from '../views/EditUser.vue'

const routes = [
  {
    path: '/',
    name: 'Landingpage',
    component: Landingpage
  },
  {
    path: "/inside",
    name: "inside",
    component: Inside
  },
  {
    path: "/edit_user",
    name: "edit user",
    component: editUser
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

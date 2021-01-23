import Vue from 'vue'
import VueRouter from 'vue-router'
import login from '@views/login.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login',
    component: login
  },
  {
    path: '/signin',
    name: 'Signin',
    component: () => import('@views/signin.vue')
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: () => import('@views/dashboard.vue')
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

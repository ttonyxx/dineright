import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import StudentSignIn from '../views/StudentSignIn.vue'
import StudentDashboard from '../views/StudentDashboard.vue'
import DiningDashboard from '../views/DiningDashboard.vue'
import StudentSignUp from '../views/StudentSignUp.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/studentsignin',
    name: 'StudentSignIn',
    component: StudentSignIn
  },
  {
    path: '/student',
    name: 'StudentDashboard',
    component: StudentDashboard
  },
  {
    path: '/dining',
    name: 'DiningDashboard',
    component: DiningDashboard
  },
  {
    path: '/studentsignup',
    component: StudentSignUp
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
